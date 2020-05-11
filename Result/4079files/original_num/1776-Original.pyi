# (generated with --quick)

import numpy
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
    def __init__(self, env, policy, config: dict, normalize_states = ..., state_preprocessor = ..., summary_writer = ...) -> None: ...
    def choose_action(self, state: numpy.ndarray) -> Any: ...
    def get_steps(self, n_steps: int, reset: bool = ..., stop_at_trajectory_end: bool = ..., render: bool = ...) -> Any: ...
    def get_trajectories(self, stop_at_trajectory_end: bool = ..., render: bool = ...) -> list: ...
    def get_trajectory(self, stop_at_trajectory_end: bool = ..., render: bool = ...) -> Any: ...
    def normalize(self, state: numpy.ndarray) -> numpy.ndarray: ...
    def reset_env(self) -> None: ...
    def state_preprocessor(self, _1) -> Any: ...
    def step_env(self, action) -> Tuple[Any, Any, Any, Any]: ...
