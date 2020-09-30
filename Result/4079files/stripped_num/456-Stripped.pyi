# (generated with --quick)

from typing import Any

BasicShapedRewardNet: Any
Trainer: Any
discrim_net: Any
util: Any

def init_trainer(env_id, rollout_glob, *, n_expert_demos = ..., seed = ..., log_dir = ..., use_gail = ..., num_vec = ..., parallel = ..., max_n_files = ..., scale = ..., airl_entropy_weight = ..., discrim_kwargs = ..., reward_kwargs = ..., trainer_kwargs = ..., make_blank_policy_kwargs = ...) -> Any: ...
