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
    def __init__(self, row: dict, context) -> None: ...

class Languages(Any):
    _members: Dict[int, Set[Language]]
    prefix: Any
    def __init__(self) -> None: ...
    def _filter_langs(self, entryid, acceptability) -> List[str]: ...
    def acceptable(self, descid) -> List[str]: ...
    def add(self, row: dict, context, _) -> None: ...
    def preferred(self, descid) -> List[str]: ...

def __getattr__(name) -> Any: ...
