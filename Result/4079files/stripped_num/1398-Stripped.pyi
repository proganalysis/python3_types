# (generated with --quick)

from typing import Any, List, Type

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
    dim: Any
    level: Any
    nn_engine: Any
    num_cfs: int
    point_to_biconode: List[BICONode]
    proj: Any
    projection_func: Any
    def __init__(self, level, dim, proj, bico, projection_func) -> None: ...
    def get_cf(self) -> list: ...
    def insert_point(self, point_cf) -> Any: ...
    def output_cf(self, f) -> None: ...
