# (generated with --quick)

from typing import Any, Tuple, TypeVar, Union

Image: module
cv2: Any
mss: Any
np: module
os: module
pyautogui: Any
time: module

_T2 = TypeVar('_T2')

class Board(object):
    gameover_template: Any
    landscape: Any
    landscape_template: Any
    shooter: Any
    x1: int
    x2: Any
    y1: Any
    y2: Any
    @staticmethod
    def compute_distance_and_size(roi, max_distance) -> Tuple[Any, Any]: ...
    def compute_speed(self, distance, last_distance, speed: _T2, last_speeds, last_compute_speed) -> Union[int, _T2]: ...
    def find_game_position(self, threshold) -> dict: ...
    def get_game_landscape_and_set_focus_or_die(self, threshold = ...) -> dict: ...
    def play_game(self, get_command_callback) -> int: ...
    @staticmethod
    def reject_outliers(values) -> Any: ...
    @staticmethod
    def reset_game() -> None: ...
    @staticmethod
    def start_game() -> None: ...
