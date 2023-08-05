# Copyright (c) 2021, salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root
# or https://opensource.org/licenses/BSD-3-Clause

"""
Example training script for the grid world and continuous versions of Tag.
Note: This training script only runs on a GPU machine.
You will also need to install WarpDrive (https://github.com/salesforce/warp-drive)
using `pip install rl-warp-drive`, and Pytorch(https://pytorch.org/)
"""

import argparse
import os

import GPUtil

from ai_economist.foundation.env_wrapper import FoundationEnvWrapper
from ai_economist.foundation.scenarios.covid19.covid19_env import (
    CovidAndEconomyEnvironment,
)

try:
    num_gpus_available = len(GPUtil.getAvailable())
    assert num_gpus_available > 0, "This training script needs a GPU machine to run!!"
    print(f"{num_gpus_available} GPUs are available.")
    import torch
    import yaml
    from warp_drive.training.trainer import Trainer
    from warp_drive.training.utils.data_loader import create_and_push_data_placeholders
    from warp_drive.utils.env_registrar import CustomizedEnvironmentRegistrar
except ValueError:
    raise ValueError("This training script needs a GPU machine to run!!") from None

pytorch_cuda_init_success = torch.cuda.FloatTensor(8)
_COVID_AND_ECONOMY_ENVIRONMENT = "covid_and_economy_environment"

# Usage:
# >> python ai_economist/training/example_training_script.py
# --env covid_and_economy_environment


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--env", "-e", type=str, help="Environment to train.")

    args = parser.parse_args()

    # Read the run configurations specific to each environment.
    # Note: The run config yamls can be edited at warp_drive/training/run_configs
    # ---------------------------------------------------------------------------
    assert args.env in [_COVID_AND_ECONOMY_ENVIRONMENT], (
        f"Currently, the only environment supported "
        f"is {_COVID_AND_ECONOMY_ENVIRONMENT}"
    )

    config_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "run_configs",
        f"run_config_{args.env}.yaml",
    )
    with open(config_path, "r") as f:
        run_config = yaml.safe_load(f)

    num_envs = run_config["trainer"]["num_envs"]

    # Create a wrapped environment object via the EnvWrapper
    # Ensure that use_cuda is set to True (in order to run on the GPU)
    # ----------------------------------------------------------------
    if run_config["name"] == _COVID_AND_ECONOMY_ENVIRONMENT:
        env_registrar = CustomizedEnvironmentRegistrar()
        this_file_dir = os.path.dirname(os.path.abspath(__file__))
        env_registrar.register_environment(
            CovidAndEconomyEnvironment.name,
            os.path.join(
                this_file_dir, "../foundation/scenarios/covid19/covid19_build.cu"
            ),
        )
        env_wrapper = FoundationEnvWrapper(
            CovidAndEconomyEnvironment(**run_config["env"]),
            num_envs=num_envs,
            use_cuda=True,
            customized_env_registrar=env_registrar,
        )
    else:
        raise NotImplementedError

    # Policy mapping to agent ids: agents can share models
    # The policy_tag_to_agent_id_map dictionary maps
    # policy model names to agent ids.
    # ----------------------------------------------------
    if len(run_config["policy"].keys()) == 1:
        # Using a single (or shared policy) across all agents
        policy_name = list(run_config["policy"])[0]
        policy_tag_to_agent_id_map = {
            policy_name: list(env_wrapper.env.taggers) + list(env_wrapper.env.runners)
        }
    else:
        # Using different policies for different(sets) of agents
        policy_tag_to_agent_id_map = {
            "a": [str(agent_id) for agent_id in range(env_wrapper.env.n_agents)],
            "p": ["p"],
        }

    # Assert that all the valid policies are mapped to at least one agent
    assert set(run_config["policy"].keys()) == set(policy_tag_to_agent_id_map.keys())

    # Flag indicating whether separate obs, actions and rewards placeholders
    # have to be created for each policy
    # Set "create_separate_placeholders_for_each_policy" to True
    # since the agents and planner have different observation
    # and action spaces.
    separate_placeholder_per_policy = True

    # Flag indicating the observation dimension corresponding to
    # 'num_agents'
    # Note: WarpDrive assumes that all the observation are shaped
    # (num_agents, *feature_dim), i.e., the observation dimension
    # corresponding to 'num_agents' is the first one. Instead, if the
    # observation dimension corresponding to num_agents is the last one,
    # we will need to permute the axes to align with WarpDrive's assumption
    obs_dim_corresponding_to_num_agents = "last"

    # Trainer object
    # --------------
    trainer = Trainer(
        env_wrapper=env_wrapper,
        config=run_config,
        policy_tag_to_agent_id_map=policy_tag_to_agent_id_map,
        create_separate_placeholders_for_each_policy=separate_placeholder_per_policy,
        obs_dim_corresponding_to_num_agents=obs_dim_corresponding_to_num_agents,
    )

    # Create and push data placeholders to the device
    # -----------------------------------------------
    create_and_push_data_placeholders(
        env_wrapper,
        policy_tag_to_agent_id_map,
        trainer,
    )

    # Perform training
    # ----------------
    trainer.train()
    trainer.graceful_close()
