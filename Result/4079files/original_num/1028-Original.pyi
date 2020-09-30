# (generated with --quick)

import __future__
from typing import Any, Callable, Optional

FLAGS: Any
absolute_import: __future__._Feature
division: __future__._Feature
flags: Any
functools: module
lt: Any
print_function: __future__._Feature
tf: Any

def bounds(lower: float, upper: float, labeled_tensor, name: Optional[str] = ...) -> Any: ...
def bounds_unlabeled(lower: float, upper: float, tensor, name: Optional[str] = ...) -> Any: ...
def shape(labeled_tensor, name: Optional[str] = ...) -> Any: ...
def shape_unlabeled(tensor, name: Optional[str] = ...) -> Any: ...
def well_defined() -> Callable[[Any], Any]: ...
