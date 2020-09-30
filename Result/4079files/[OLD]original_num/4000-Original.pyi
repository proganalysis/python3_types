# (generated with --quick)

from typing import Any

Poster: Any
ValueRange: Any
XY: Any
argparse: module
svgwrite: Any
utils: Any

class TracksDrawer:
    __doc__: str
    poster: Any
    def __init__(self, the_poster) -> None: ...
    def color(self, length_range, length: float, is_special: bool = ...) -> str: ...
    def create_args(self, args_parser: argparse.ArgumentParser) -> None: ...
    def draw(self, d, size, offset) -> None: ...
    def fetch_args(self, args) -> None: ...
