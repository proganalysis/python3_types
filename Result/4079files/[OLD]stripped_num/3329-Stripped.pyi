# (generated with --quick)

import collections
from typing import Any, Type

check_argument_types: Any
defaultdict: Type[collections.defaultdict]
load: Any

class PluginCache(collections.defaultdict):
    __doc__: str
    namespace: Any
    def __getattr__(self, name) -> Any: ...
    def __init__(self, namespace) -> None: ...
    def __missing__(self, key) -> Any: ...
