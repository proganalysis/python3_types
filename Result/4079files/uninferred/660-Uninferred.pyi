from .xy import XY
from typing import Any

class Poster:
    athlete: Any = ...
    title: str = ...
    tracks_by_date: Any = ...
    tracks: Any = ...
    length_range: Any = ...
    length_range_by_date: Any = ...
    units: str = ...
    colors: Any = ...
    width: int = ...
    height: int = ...
    years: Any = ...
    tracks_drawer: Any = ...
    def __init__(self) -> None: ...
    def set_tracks(self, tracks: Any) -> None: ...
    def draw(self, drawer: Any, output: Any) -> None: ...
    def m2u(self, m: Any): ...
    def u(self): ...
    def __draw_tracks(self, d: Any, size: XY, offset: XY) -> Any: ...
    def __draw_header(self, d: Any) -> None: ...
    def __draw_footer(self, d: Any) -> None: ...
    def __compute_track_statistics(self): ...
    def __compute_years(self, tracks: Any) -> None: ...
