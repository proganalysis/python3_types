# (generated with --quick)

from typing import Any, Callable

maxout: Any
multilayer_projection: Any
tf: Any

def maxout_output(maxout_size) -> Callable[[Any, Any, Any], Any]: ...
def mlp_output(layer_sizes, dropout_keep_prob = ..., train_mode = ..., activation = ...) -> Callable[[Any, Any, Any], Any]: ...
def no_deep_output(prev_state, prev_output, ctx_tensors) -> Any: ...
