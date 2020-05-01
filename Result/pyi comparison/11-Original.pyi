# (generated with --quick)

from typing import Callable, List, SupportsFloat

Image: module
json: module

def floor(__x: SupportsFloat) -> int: ...
def process_image(input_path: str, output_path: str) -> None: ...
def process_line(getter: Callable, color_predicate: Callable, size) -> List[int]: ...
