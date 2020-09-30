# (generated with --quick)

import io
import json.decoder
from typing import Any, Callable, List, Optional, Tuple, Type, Union

ALLOWED_HOSTS: Any
BBox: Any
BytesIO: Type[io.BytesIO]
Color: Any
Geometry: Any
IMAGE_SIZE: Tuple[int, int]
Image: module
ImageDraw: module
PORT: Any
Proj: Any
TILE_SIZE: Tuple[int, int]
aiohttp: Any
asyncio: module
image_to_world: Any
math: module
mercantile: Any
settings: Any
sys: module
transform: Any
world_to_image: Any

class MapImage(object):
    _basemap_image: Any
    basemap: Any
    image_bbox: Any
    image_size: Tuple[int, int]
    num_tiles: List[int]
    opacity: Any
    point: Any
    point_px: list
    target_size: Any
    to_image: Any
    to_world: Any
    ul_tile: Any
    zoom: Any
    def __init__(self, center, bbox, zoom, basemap, opacity, size = ...) -> None: ...
    def _configure_event_loop(self) -> None: ...
    def crop_image(self, im) -> Tuple[Any, Any]: ...
    def draw_geometry(self, im, geometry, color, width) -> None: ...
    def get_image(self, service_url) -> Tuple[Any, Any]: ...
    def get_layer_images(self, service_url) -> list: ...
    def get_legend(self, legend_url) -> Any: ...
    def get_polygon_image(self, polygons) -> Tuple[Any, Any]: ...

def loads(s: Union[bytearray, bytes, str], encoding = ..., cls: Optional[Type[json.decoder.JSONDecoder]] = ..., object_hook: Optional[Callable[[dict], Any]] = ..., parse_float: Optional[Callable[[str], Any]] = ..., parse_int: Optional[Callable[[str], Any]] = ..., parse_constant: Optional[Callable[[str], Any]] = ..., object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = ..., **kwds) -> Any: ...
