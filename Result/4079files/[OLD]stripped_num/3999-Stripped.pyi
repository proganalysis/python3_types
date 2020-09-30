# (generated with --quick)

from typing import Any, Callable, Tuple, Type, TypeVar, Union

OutputProjection = Callable[[Any, Any, list, Any], Any]

OutputProjectionSpec: Type[Union[Callable[[Any, Any, list, Any], Any], Tuple[Callable[[Any, Any, list, Any], Any], int]]]
check_argument_types: Any
dropout: Any
get_initializer: Any
maxout: Any
multilayer_projection: Any
tf: Any

_T0 = TypeVar('_T0')

def _legacy_linear(output_size: _T0) -> Tuple[Callable[[Any, Any, Any, Any], Any], _T0]: ...
def _legacy_relu(output_size: _T0) -> Tuple[Callable[[Any, Any, Any, Any], Any], _T0]: ...
def maxout_output(maxout_size: _T0) -> Tuple[Callable[[Any, Any, Any, Any], Any], _T0]: ...
def mlp_output(layer_sizes, activation = ..., dropout_keep_prob = ...) -> Tuple[Callable[[Any, Any, Any, Any], Any], Any]: ...
def nematus_output(output_size: _T0, activation_fn = ..., dropout_keep_prob = ...) -> Tuple[Callable[[Any, Any, Any, Any], Any], _T0]: ...
def nonlinear_output(output_size: _T0, activation_fn = ...) -> Tuple[Callable[[Any, Any, Any, Any], Any], _T0]: ...
