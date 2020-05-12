import tensorflow as tf
from demeter.rl import Policy, Transition, TransitionAlgorithm
from typing import Any

__all__: Any

class Reinforce(TransitionAlgorithm):
    actor: Any = ...
    policy_obj_model: Any = ...
    optimizer: Any = ...
    discount: Any = ...
    step_batch_size: Any = ...
    episode_batch_size: Any = ...
    steps: int = ...
    episodes: int = ...
    buffer: Any = ...
    step_counter: Any = ...
    def __init__(self, actor: Policy, policy_obj_model: tf.keras.Model, optimizer: tf.train.Optimizer, discount: float, step_batch_size: int=..., episode_batch_size: int=...) -> None: ...
    def transition_update(self, transition: Transition, *args: Any, **kwargs: Any) -> None: ...
    def _update_batch(self) -> None: ...
    def _add_to_buffer(self, transition: Transition, **kwargs: Any) -> None: ...
