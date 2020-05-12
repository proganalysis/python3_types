# (generated with --quick)

from typing import Any

ArmaNodes: Any
MovementDirectorAbstract: Any
__author__: str
__email__: str
singletons: Any

class MovementDirectorArma(Any):
    __doc__: str
    node_count: Any
    nodes: Any
    def __init__(self, node_count, file_path) -> None: ...
    def get_distances_from_nodes(self) -> Any: ...
    def get_geo_json_for_nodes(self) -> Any: ...
    def get_geo_json_for_roads(self) -> str: ...
    def set_path_to_replay_file(self, path) -> None: ...
    def simulate_one_step(self) -> None: ...
