# (generated with --quick)

from typing import Any, Tuple

AttentionLoopStateTA: Any
BaseAttention: Any
InitializerSpecs: Any
Stateful: Any
check_argument_types: Any
empty_attention_loop_state: Any
tensor: Any
tf: Any

class StatefulContext(Any):
    __doc__: str
    attention_mask: Any
    attention_states: Any
    context_vector_size: Any
    encoder: Any
    state_size: Any
    def __init__(self, name, encoder, save_checkpoint = ..., load_checkpoint = ..., initializers = ...) -> None: ...
    def attention(self, query, decoder_prev_state, decoder_input, loop_state, step) -> Tuple[Any, Any]: ...
    def finalize_loop(self, key, last_loop_state) -> None: ...
    def initial_loop_state(self) -> Any: ...
    def visualize_attention(self, key) -> None: ...
