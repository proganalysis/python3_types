# (generated with --quick)

from typing import Any

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
    _batch_size: Any
    _discount: Any
    _epsilon: Any
    _forward: Any
    _min_replay_size: Any
    _num_actions: Any
    _online_network: Any
    _optimizer: Any
    _replay: Any
    _rng: Any
    _sgd_period: Any
    _target_network: Any
    _target_update_period: Any
    _total_steps: int
    _training_step: Any
    def __init__(self, action_spec, online_network, target_network, batch_size, discount, replay_capacity, min_replay_size, sgd_period, target_update_period, optimizer, epsilon, seed = ...) -> None: ...
    def policy(self, timestep) -> Any: ...
    def update(self, timestep, action, new_timestep) -> None: ...

def default_agent(obs_spec, action_spec) -> DQNTF2: ...
