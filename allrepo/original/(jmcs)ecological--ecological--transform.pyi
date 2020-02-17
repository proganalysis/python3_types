# (generated with --quick)

from typing import Any, Dict, List, Type, Union

Counter: Any
Deque: Any
GenericMeta: Any
PEP560: bool
TYPES_THAT_NEED_TO_BE_PARSED: List[Type[Union[bool, dict, list, set, tuple]]]
TYPING_TO_REGULAR_TYPE: Dict[Any, type]
_NOT_IMPORTED: Any
ast: module
collections: module

def _cast_typing_old(wanted_type: type) -> type: ...
def _cast_typing_pep560(wanted_type: type) -> type: ...
def cast(representation: str, wanted_type: type) -> Any: ...
