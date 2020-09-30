# (generated with --quick)

from typing import Any, Callable, Dict, Iterable, Optional, Type, TypeVar

BELGraph: Any
Manager: Any

_T = TypeVar('_T')

class DictManager(Any):
    __doc__: str
    disease_to_id: Dict[nothing, nothing]
    hash_to_node: Dict[nothing, nothing]
    networks: Dict[int, Any]
    universe: None
    def __init__(self, connection: Optional[str] = ...) -> None: ...
    def get_graph_by_id(self, network_id: int) -> Any: ...
    def get_graphs_by_ids(self, network_ids: Iterable[int]) -> list: ...
    def insert_graph(self, graph, **_kwargs) -> _Namespace: ...

class _Namespace:
    id: int
    def __init__(self, id: int) -> None: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
