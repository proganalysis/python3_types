# (generated with --quick)

from typing import Any, Dict, List, Union

class C3Nav35C3(MapSource):
    attribution: str
    bounds: List[List[float]]
    hack_257px: bool
    level_config: List[List[int]]
    max_zoom: int
    min_zoom: int
    simple_crs: bool
    tileserver: str

class MapSource(metaclass=_MapSourceType):
    @classmethod
    def get(cls, attr, default = ...) -> Any: ...
    @classmethod
    def override(cls, attr, value) -> None: ...

class OpenStreetMapCamp2019(MapSource):
    attribution: str
    initial_view: Dict[str, Union[float, int]]
    max_zoom: int
    min_zoom: int
    tileserver: str
    tileserver_subdomains: List[str]

class _MapSourceType(type):
    def __getattr__(cls: _MapSourceType, attr) -> None: ...
