# (generated with --quick)

from typing import Any, Dict, List, Set, Type

LanguageName: Type[str]
RF2File: Any
TransformationContext: Any
Transitive: Any

class Language:
    __doc__: str
    acceptabilityId: int
    lang: Any
    def __init__(self, row, context) -> None: ...

class Languages(Any):
    _members: Dict[int, Set[Language]]
    prefix: Any
    def __init__(self) -> None: ...
    def _filter_langs(self, entryid, acceptability) -> List[nothing]: ...
    def acceptable(self, descid) -> Any: ...
    def add(self, row, context, _) -> None: ...
    def preferred(self, descid) -> Any: ...

def __getattr__(name) -> Any: ...
