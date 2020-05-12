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
    def color(self, length_range, length, is_special = ...) -> Any: ...
    def create_args(self, args_parser) -> None: ...
    def draw(self, d, size, offset) -> None: ...
    def fetch_args(self, args) -> None: ...
