# (generated with --quick)

from typing import Any, Callable, List, Tuple, Type, Union

OutputProjection = Callable[[Any, Any, list, Any], Any]

OutputProjectionSpec: Type[Union[Callable[[Any, Any, list, Any], Any], Tuple[Callable[[Any, Any, list, Any], Any], int]]]
check_argument_types: Any
dropout: Any
get_initializer: Any
maxout: Any
multilayer_projection: Any
tf: Any

def _legacy_linear(output_size: int) -> Tuple[Callable[[Any, Any, list, Any], Any], int]: ...
def _legacy_relu(output_size: int) -> Tuple[Callable[[Any, Any, list, Any], Any], int]: ...
def maxout_output(maxout_size: int) -> Tuple[Callable[[Any, Any, list, Any], Any], int]: ...
def mlp_output(layer_sizes: List[int], activation: Callable[[Any], Any] = ..., dropout_keep_prob: float = ...) -> Tuple[Callable[[Any, Any, list, Any], Any], int]: ...
def nematus_output(output_size: int, activation_fn: Callable[[Any], Any] = ..., dropout_keep_prob: float = ...) -> Tuple[Callable[[Any, Any, list, Any], Any], int]: ...
def nonlinear_output(output_size: int, activation_fn: Callable[[Any], Any] = ...) -> Tuple[Callable[[Any, Any, list, Any], Any], int]: ...
