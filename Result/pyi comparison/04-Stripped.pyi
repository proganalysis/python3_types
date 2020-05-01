# (generated with --quick)

import collections
from typing import Any, Type

check_argument_types: Any
deque: Type[collections.deque]
load: Any
nodefault: Any

class Importer:
    __slots__ = ["executable", "namespace", "protect", "redirects", "separators"]
    __doc__: str
    executable: Any
    namespace: Any
    protect: Any
    redirects: collections.deque
    separators: Any
    def __call__(self, target, default = ...) -> Any: ...
    def __init__(self, redirect = ..., namespace = ..., separators = ..., executable = ..., protect = ...) -> None: ...
    def redirect(self, source, destination) -> None: ...
