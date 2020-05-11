# (generated with --quick)

from typing import Any, List, Optional

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
    discount: float
    episode_batch_size: Optional[int]
    episodes: int
    optimizer: Any
    policy_obj_model: Any
    step_batch_size: Optional[int]
    step_counter: Any
    steps: int
    def __init__(self, actor, policy_obj_model, optimizer, discount: float, step_batch_size: Optional[int] = ..., episode_batch_size: Optional[int] = ...) -> None: ...
    def _add_to_buffer(self, transition, **kwargs) -> None: ...
    def _update_batch(self) -> None: ...
    def transition_update(self, transition, *args, **kwargs) -> None: ...
