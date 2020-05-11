# (generated with --quick)

from typing import Any, Callable, List, Tuple

Image: module
cv2: Any
mss: Any
np: module
os: module
pyautogui: Any
time: module

class Board(object):
    gameover_template: Any
    landscape: dict
    landscape_template: Any
    shooter: Any
    x1: int
    x2: Any
    y1: Any
    y2: Any
    @staticmethod
    def compute_distance_and_size(roi, max_distance: int) -> Tuple[Any, Any]: ...
    def compute_speed(self, distance: int, last_distance: int, speed: int, last_speeds: List[float], last_compute_speed: float) -> int: ...
    def find_game_position(self, threshold) -> dict: ...
    def get_game_landscape_and_set_focus_or_die(self, threshold = ...) -> dict: ...
    def play_game(self, get_command_callback: Callable[[int, int, int], str]) -> int: ...
    @staticmethod
    def reject_outliers(values: List[float]) -> Any: ...
    @staticmethod
    def reset_game() -> None: ...
    @staticmethod
    def start_game() -> None: ...
