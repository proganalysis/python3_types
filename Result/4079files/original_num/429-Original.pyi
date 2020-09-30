# (generated with --quick)

import collections
from typing import Any, Type

OrderedDict: Type[collections.OrderedDict]
TorchTrainer: Any
create_stats_ordered_dict: Any
nn: Any
np: module
optim: Any
ptu: Any
torch: Any

class DDPGTrainer(Any):
    __doc__: str
    _n_train_steps_total: int
    _need_to_update_eval_statistics: bool
    discount: Any
    eval_statistics: collections.OrderedDict[str, Any]
    max_q_value: Any
    min_q_value: Any
    networks: list
    policy_learning_rate: Any
    policy_optimizer: Any
    policy_pre_activation_weight: Any
    qf_criterion: Any
    qf_learning_rate: Any
    qf_optimizer: Any
    qf_weight_decay: Any
    reward_scale: Any
    target_hard_update_period: Any
    tau: Any
    use_soft_update: Any
    def __init__(self, qf, target_qf, policy, target_policy, discount = ..., reward_scale = ..., policy_learning_rate = ..., qf_learning_rate = ..., qf_weight_decay = ..., target_hard_update_period = ..., tau = ..., use_soft_update = ..., qf_criterion = ..., policy_pre_activation_weight = ..., optimizer_class = ..., min_q_value = ..., max_q_value = ...) -> None: ...
    def _update_target_networks(self) -> None: ...
    def end_epoch(self, epoch) -> None: ...
    def get_diagnostics(self) -> collections.OrderedDict[str, Any]: ...
    def get_epoch_snapshot(self) -> dict: ...
    def policy(self, _1) -> Any: ...
    def qf(self, _1, _2) -> Any: ...
    def target_policy(self, _1) -> Any: ...
    def target_qf(self, _1, _2) -> Any: ...
    def train_from_torch(self, batch) -> None: ...
