# (generated with --quick)

from typing import Any, Optional, Tuple

DBSCAN: Any
MDS: Any
build_nx_from_metadata: Any
dendrogram: Any
linkage: Any
np: module
nx: module
os: module
pd: Any
plt: Any
sns: Any
squareform: Any

class PWEVisualization:
    @staticmethod
    def cluster_map_viz(dist_matrix, pw_ids: Optional[list] = ..., cmap = ...) -> Any: ...
    @staticmethod
    def dbscan_clustering(dist_matrix, save_to_file = ...) -> Tuple[Any, Any]: ...
    @staticmethod
    def graphviz_from_meta_data(pw_rel_dfs, graphviz_meta_data) -> Any: ...
    @staticmethod
    def linkage_dendrogram(dist_matrix, pws_used: Optional[list] = ..., save_to_folder = ...) -> list: ...
    @staticmethod
    def mds_networkx(pws_used, A, scale_down_factor, save_to_file = ...) -> Any: ...
    @staticmethod
    def mds_sklearn(A, save_to_file = ...) -> Any: ...
