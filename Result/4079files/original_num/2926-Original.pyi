# (generated with --quick)

from typing import Any, Optional, SupportsFloat, TypeVar, Union

nan: float
rename_keys: Any
replace_keys: Any

_T0 = TypeVar('_T0')

def isnan(__x: SupportsFloat) -> bool: ...
def nan_to_none(value: _T0) -> Optional[_T0]: ...
def none_to_nan(value: _T0) -> Union[float, _T0]: ...
