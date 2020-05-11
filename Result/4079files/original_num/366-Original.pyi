# (generated with --quick)

from typing import Any, Coroutine, List, Type

Api: Any
AssEvent: Any
BLACK_THRESHOLD: int
BaseCommand: Any
COMMANDS: List[Type[DetectKaraokeCommand]]
CommandUnavailable: Any
DIFF_THRESHOLD: int
FRAME_CROP: int
FRAME_HEIGHT: int
FRAME_WIDTH: int
MENU: list
MenuCommand: Any
Pts: Any
WHITE_THRESHOLD: int
argparse: module
bisect: module
cv2: Any
ex: ImportError
ms_to_str: Any
np: module

class DetectKaraokeCommand(Any):
    help_text: str
    is_enabled: Any
    names: List[str]
    def add_sub(self, start: int, end: int) -> None: ...
    @staticmethod
    def decorate_parser(api, parser: argparse.ArgumentParser) -> None: ...
    def get_frame(self, frame_idx: int) -> Any: ...
    def run(self) -> Coroutine[Any, Any, None]: ...

def is_black(frame) -> bool: ...
def is_white(frame) -> bool: ...
