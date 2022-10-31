import numpy as np
from bico.nearest_neighbor.base import NearestNeighbor as NearestNeighbor
from bico.utils.ClusteringFeature import ClusteringFeature
from typing import Any, Callable, List, TextIO

logger: Any

class BICONode:
    level: Any = ...
    dim: Any = ...
    proj: Any = ...
    point_to_biconode: Any = ...
    projection_func: Any = ...
    nn_engine: Any = ...
    num_cfs: int = ...
    bico: Any = ...
    cf: Any = ...
    def __init__(self, level: int, dim: int, proj: int, bico: BICO, projection_func: Callable[[int, int, float], NearestNeighbor]) -> None: ...
    def insert_point(self, point_cf: ClusteringFeature) -> int: ...
    def output_cf(self, f: TextIO) -> None: ...
    def get_cf(self) -> List[np.ndarray]: ...