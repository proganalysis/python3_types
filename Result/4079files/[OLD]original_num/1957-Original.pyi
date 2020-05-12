# (generated with --quick)

from typing import Any, Optional, Tuple

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
    context_vector_size: int
    encoder: Any
    state_size: int
    def __init__(self, name: str, encoder, save_checkpoint: Optional[str] = ..., load_checkpoint: Optional[str] = ..., initializers = ...) -> None: ...
    def attention(self, query, decoder_prev_state, decoder_input, loop_state, step) -> Tuple[Any, Any]: ...
    def finalize_loop(self, key: str, last_loop_state) -> None: ...
    def initial_loop_state(self) -> Any: ...
    def visualize_attention(self, key: str) -> None: ...
