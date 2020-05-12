# (generated with --quick)

from typing import Any, List

Policy: Any
TensorBuffer: Any
Transition: Any
TransitionAlgorithm: Any
__all__: List[str]
np_utils: Any
tf: Any

class Reinforce(Any):
    actor: Any
    buffer: Any
    discount: Any
    episode_batch_size: Any
    episodes: int
    optimizer: Any
    step_batch_size: Any
    step_counter: Any
    steps: int
    def __init__(self, actor, policy_obj_model, optimizer, discount, step_batch_size = ..., episode_batch_size = ...) -> None: ...
    def _add_to_buffer(self, transition, **kwargs) -> None: ...
    def _update_batch(self) -> None: ...
    def policy_obj_model(self) -> Any: ...
    def transition_update(self, transition, *args, **kwargs) -> None: ...
