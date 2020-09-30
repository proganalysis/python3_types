# (generated with --quick)

from typing import Any, Optional

base: Any
dm_env: Any
np: module
qlearning: Any
replay: Any
snt: Any
specs: Any
tf: Any

class DQNTF2(Any):
    __doc__: str
    _batch_size: int
    _discount: float
    _epsilon: float
    _forward: Any
    _min_replay_size: int
    _num_actions: Any
    _online_network: Any
    _optimizer: Any
    _replay: Any
    _rng: Any
    _sgd_period: int
    _target_network: Any
    _target_update_period: int
    _total_steps: int
    _training_step: Any
    def __init__(self, action_spec, online_network, target_network, batch_size: int, discount: float, replay_capacity: int, min_replay_size: int, sgd_period: int, target_update_period: int, optimizer, epsilon: float, seed: Optional[int] = ...) -> None: ...
    def policy(self, timestep) -> Any: ...
    def update(self, timestep, action, new_timestep) -> None: ...

def default_agent(obs_spec, action_spec) -> DQNTF2: ...
