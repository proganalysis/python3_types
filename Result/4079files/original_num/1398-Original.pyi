# (generated with --quick)

import numpy
from typing import Any, Callable, List, TextIO, Type

ClusteringFeature: Any
NearestNeighbor: Any
Point: Any
datetime: Type[datetime.datetime]
logger: logging.Logger
logging: module
np: module

class BICONode:
    bico: Any
    cf: Any
    dim: int
    level: int
    nn_engine: Any
    num_cfs: int
    point_to_biconode: List[BICONode]
    proj: int
    projection_func: Callable[[int, int, float], Any]
    def __init__(self, level: int, dim: int, proj: int, bico, projection_func: Callable[[int, int, float], Any]) -> None: ...
    def get_cf(self) -> List[numpy.ndarray]: ...
    def insert_point(self, point_cf) -> int: ...
    def output_cf(self, f: TextIO) -> None: ...
