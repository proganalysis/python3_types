# (generated with --quick)

from typing import Any, Tuple

Experience: Any
ExperiencesMemory: Any
RunningMeanStd: Any
normalize: Any
np: module
tf: Any

class EnvRunner(object):
    __doc__: str
    config: dict
    env: Any
    episode_reward: Any
    episode_steps: int
    features: Any
    n_episodes: int
    normalize_states: Any
    policy: Any
    rms: Any
    state: Any
    summary_writer: Any
    def __init__(self, env, policy, config, normalize_states = ..., state_preprocessor = ..., summary_writer = ...) -> None: ...
    def choose_action(self, state) -> Any: ...
    def get_steps(self, n_steps, reset = ..., stop_at_trajectory_end = ..., render = ...) -> Any: ...
    def get_trajectories(self, stop_at_trajectory_end = ..., render = ...) -> list: ...
    def get_trajectory(self, stop_at_trajectory_end = ..., render = ...) -> Any: ...
    def normalize(self, state) -> Any: ...
    def reset_env(self) -> None: ...
    def state_preprocessor(self, _1) -> Any: ...
    def step_env(self, action) -> Tuple[Any, Any, Any, Any]: ...
