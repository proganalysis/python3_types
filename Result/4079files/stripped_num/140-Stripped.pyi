# (generated with --quick)

from typing import Any, Dict, List, Type, TypeVar, Union

Counter: Any
Deque: Any
GenericMeta: Any
PEP560: bool
TYPES_THAT_NEED_TO_BE_PARSED: List[Type[Union[bool, dict, list, set, tuple]]]
TYPING_TO_REGULAR_TYPE: Dict[Any, type]
_NOT_IMPORTED: Any
ast: module
collections: module

_T0 = TypeVar('_T0')

def _cast_typing_old(wanted_type: _T0) -> Union[type, _T0]: ...
def _cast_typing_pep560(wanted_type) -> Any: ...
def cast(representation, wanted_type) -> Any: ...
