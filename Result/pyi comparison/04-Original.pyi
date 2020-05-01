# (generated with --quick)

import collections
from typing import Any, Iterable, Optional, Sequence, Type

check_argument_types: Any
deque: Type[collections.deque]
load: Any
nodefault: Any

class Importer:
    __slots__ = ["executable", "namespace", "protect", "redirects", "separators"]
    __doc__: str
    executable: bool
    namespace: Optional[str]
    protect: bool
    redirects: collections.deque
    separators: Sequence[str]
    def __call__(self, target: str, default = ...) -> Any: ...
    def __init__(self, redirect: Optional[Iterable[Sequence[str]]] = ..., namespace: Optional[str] = ..., separators: Sequence[str] = ..., executable: bool = ..., protect: bool = ...) -> None: ...
    def redirect(self, source: str, destination: str) -> None: ...
