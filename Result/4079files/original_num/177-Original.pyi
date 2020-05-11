# (generated with --quick)

from typing import Any, TypeVar

ActorCriticNetworkContinuous: Any
ActorCriticNetworkDiscrete: Any
ActorCriticNetworkDiscreteCNN: Any
ActorCriticNetworkDiscreteCNNRNN: Any
Agent: Any
EnvRunner: Any
FastSaver: Any
actor_critic_continuous_loss: Any
actor_critic_discrete_loss: Any
discount_rewards: Any
logging: module
np: module
os: module
tf: Any
wrappers: Any

_T0 = TypeVar('_T0')

class A2C(Any):
    __doc__: str
    _global_step: Any
    ac_net: None
    action: Any
    actions_taken: Any
    actor_loss: Any
    advantage: Any
    critic_loss: Any
    env: Any
    env_runner: Any
    global_step: Any
    init_op: Any
    initial_features: None
    loss: Any
    loss_summary_op: Any
    monitor_path: str
    n_steps: Any
    optimizer: Any
    ret: Any
    saver: Any
    session: Any
    states: Any
    train_op: Any
    vars: Any
    writer: Any
    def __init__(self, env, monitor_path: str, video: bool = ..., **usercfg) -> None: ...
    def _initialize(self) -> None: ...
    def build_networks(self) -> NotImplementedError: ...
    def choose_action(self, state, features) -> dict: ...
    def get_critic_value(self, state, features) -> Any: ...
    def get_env_action(self, action) -> int: ...
    def learn(self) -> None: ...
    def make_loss(self) -> NotImplementedError: ...

class A2CContinuous(A2C):
    _global_step: Any
    ac_net: Any
    action: Any
    actions_taken: Any
    actor_loss: Any
    advantage: Any
    critic_loss: Any
    env: Any
    env_runner: Any
    init_op: Any
    initial_features: None
    loss: Any
    loss_summary_op: Any
    monitor_path: str
    n_steps: Any
    optimizer: Any
    ret: Any
    saver: Any
    session: Any
    states: Any
    train_op: Any
    vars: Any
    writer: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def build_networks(self) -> None: ...
    def get_env_action(self, action: _T0) -> _T0: ...
    def make_loss(self) -> Any: ...

class A2CDiscrete(A2C):
    _global_step: Any
    ac_net: Any
    action: Any
    actions_taken: Any
    actor_loss: Any
    advantage: Any
    critic_loss: Any
    env: Any
    env_runner: Any
    init_op: Any
    initial_features: None
    loss: Any
    loss_summary_op: Any
    monitor_path: str
    n_steps: Any
    optimizer: Any
    ret: Any
    saver: Any
    session: Any
    states: Any
    train_op: Any
    vars: Any
    writer: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def build_networks(self) -> None: ...
    def make_loss(self) -> Any: ...

class A2CDiscreteCNN(A2CDiscrete):
    _global_step: Any
    ac_net: Any
    action: Any
    actions_taken: Any
    actor_loss: Any
    advantage: Any
    critic_loss: Any
    env: Any
    env_runner: Any
    init_op: Any
    initial_features: None
    loss: Any
    loss_summary_op: Any
    monitor_path: str
    n_steps: Any
    optimizer: Any
    ret: Any
    saver: Any
    session: Any
    states: Any
    train_op: Any
    vars: Any
    writer: Any

class A2CDiscreteCNNRNN(A2CDiscrete):
    _global_step: Any
    ac_net: Any
    action: Any
    actions_taken: Any
    actor_loss: Any
    advantage: Any
    critic_loss: Any
    env: Any
    env_runner: Any
    init_op: Any
    initial_features: Any
    loss: Any
    loss_summary_op: Any
    monitor_path: str
    n_steps: Any
    optimizer: Any
    ret: Any
    saver: Any
    session: Any
    states: Any
    train_op: Any
    vars: Any
    writer: Any
    def get_critic_value(self, states, features) -> Any: ...
