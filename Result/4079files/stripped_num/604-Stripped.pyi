# (generated with --quick)

import __future__
from typing import Any, List, Tuple, TypeVar, Union

heapq: module
hier: Any
np: module
print_function: __future__._Feature
scidist: Any
silhouette_score: Any
vectors: Any
words: Any

_T0 = TypeVar('_T0')

class Cluster:
    distance: Any
    left: Any
    right: Any
    def __init__(self, left, right, distance) -> None: ...
    def is_cluster(self) -> bool: ...

class DataPoint:
    label: Any
    vector: Any
    def __init__(self, label, vector) -> None: ...
    def is_cluster(self) -> bool: ...

class PreclusterMaker:
    _dist_step: Any
    _max_dist: Any
    _min_dist: Any
    linkage: Any
    metric: Any
    number_of_steps: Any
    vectors: Any
    words: Any
    def __call__(self) -> list: ...
    def __init__(self, words, vectors, number_of_steps = ..., metric = ..., linkage = ...) -> None: ...
    def _create_clusterings(self, dendrogram: _T0) -> List[List[Tuple[Any, _T0]]]: ...
    def _find_optimal_clustering(self, clusterings) -> Any: ...
    def _linkage_matrix_to_dendrogram(self, linkage_matrix, labels, vectors) -> Union[Cluster, DataPoint]: ...

def _get_cluster_nodes(node) -> Any: ...
