# (generated with --quick)

from typing import Any, Optional

BasicShapedRewardNet: Any
Trainer: Any
discrim_net: Any
util: Any

def init_trainer(env_id: str, rollout_glob: str, *, n_expert_demos: Optional[int] = ..., seed: int = ..., log_dir: Optional[str] = ..., use_gail: bool = ..., num_vec: int = ..., parallel: bool = ..., max_n_files: int = ..., scale: bool = ..., airl_entropy_weight: float = ..., discrim_kwargs: bool = ..., reward_kwargs: bool = ..., trainer_kwargs: bool = ..., make_blank_policy_kwargs: bool = ...) -> Any: ...
