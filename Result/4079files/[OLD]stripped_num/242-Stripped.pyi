# (generated with --quick)

from typing import Any, Tuple

mujoco_env: Any
np: module
point_mass_maze: Any
utils: Any

class PointMazeEnv(Any, Any):
    direction: Any
    episode_length: int
    length: Any
    max_episode_length: Any
    no_reward: Any
    sparse_reward: Any
    def __init__(self, direction = ..., maze_length = ..., sparse_reward = ..., no_reward = ..., episode_length = ...) -> None: ...
    def _get_obs(self) -> Any: ...
    def plot_trajs(self, *args, **kwargs) -> None: ...
    def reset_model(self) -> Any: ...
    def step(self, a) -> Tuple[Any, Any, bool, dict]: ...
    def viewer_setup(self) -> None: ...
