# (generated with --quick)

import collections
import functools
import itertools
from typing import Any, Callable, Optional, Tuple, Type, TypeVar

MultiPolygon: Any
Polygon: Any
chain: Type[itertools.chain]
deque: Type[collections.deque]
get_face_indizes: functools._lru_cache_wrapper
np: module
triangle: Any

_T = TypeVar('_T')

def _triangulate_polygon(polygon, keep_holes = ...) -> Tuple[Any, Any]: ...
def lru_cache(maxsize: Optional[int] = ..., typed: bool = ...) -> Callable[[Callable[..., _T]], functools._lru_cache_wrapper[_T]]: ...
def triangulate_gapless_mesh_from_polygons(geometries) -> Tuple[Any, Any]: ...
def triangulate_polygon(geometry, keep_holes = ...) -> Tuple[Any, Any]: ...
def triangulate_rings(rings, holes = ...) -> Tuple[Any, Any]: ...
