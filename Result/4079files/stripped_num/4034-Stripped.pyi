# (generated with --quick)

from typing import Any, Callable, Dict, List, Tuple

ANALOGOUS_TO: Any
ASSOCIATION: Any
BELGraph: Any
BIOMARKER_FOR: Any
BaseEntity: Any
CAUSES_NO_CHANGE: Any
DECREASES: Any
DIRECTLY_DECREASES: Any
DIRECTLY_INCREASES: Any
EQUIVALENT_TO: Any
HAS_COMPONENT: Any
HAS_MEMBER: Any
HAS_PRODUCT: Any
HAS_REACTANT: Any
HAS_VARIANT: Any
INCREASES: Any
IS_A: Any
NEGATIVE_CORRELATION: Any
POSITIVE_CORRELATION: Any
PROGONSTIC_BIOMARKER_FOR: Any
RATE_LIMITING_STEP_OF: Any
REGULATES: Any
RELATION: Any
SUBPROCESS_OF: Any
TRANSCRIBED_TO: Any
TRANSLATED_TO: Any
__all__: List[str]
default_edge_ranking: Dict[Any, int]
get_nodes_in_all_shortest_paths: Any
itt: module
nx: module
pairwise: Any

def _get_shortest_path_between_subgraphs_helper(graph, a, b) -> list: ...
def find_root_in_path(graph, path_nodes) -> Tuple[Any, Any]: ...
def get_shortest_directed_path_between_subgraphs(graph, a, b) -> list: ...
def get_shortest_undirected_path_between_subgraphs(graph, a, b) -> Any: ...
def itemgetter(*items) -> Callable[[Any], tuple]: ...
def rank_path(graph, path, edge_ranking = ...) -> Any: ...
