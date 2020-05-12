import numpy as np
from typing import Any, Generator, Iterable, Tuple

CLASS_MAPPING: Any

def load_iris_dataset() -> Tuple[np.ndarray, np.ndarray]: ...

inputs: Any
expected_outputs: Any
NUM_INPUTS: int
NUM_CLASSES: Any
NUM_HIDDEN_LAYER_NODES: int
LEARNING_RATE: float
x: Any
y: Any
yo: Any
weights: Any
biases: Any
hidden_layer: Any
logits_output_layer: Any
softmax_output_layer: Any
prediction: Any
loss: Any
optimizer: Any
train_operation: Any

def batch(iterable: Iterable, batch_size: int) -> Generator[list, None, None]: ...

NUM_EPOCHS: int
BATCH_SIZE: int
DISPLAY_ACC_EVERY_N_STEPS: int
var_initializer: Any
step: int
batches_x: Any
batches_y: Any
step_inputs: Any
all_inputs: Any
final_loss: Any
