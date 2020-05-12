from typing import Any

PEP560: bool
_NOT_IMPORTED: Any
Deque = _NOT_IMPORTED
Counter = _NOT_IMPORTED
TYPES_THAT_NEED_TO_BE_PARSED: Any
TYPING_TO_REGULAR_TYPE: Any

def _cast_typing_old(wanted_type: type) -> type: ...
def _cast_typing_pep560(wanted_type: type) -> type: ...
def cast(representation: str, wanted_type: type) -> Any: ...
