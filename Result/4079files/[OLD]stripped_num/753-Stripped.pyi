# (generated with --quick)

import numpy
from typing import Any, Dict, Generator, Tuple

BATCH_SIZE: int
CLASS_MAPPING: Dict[str, int]
DISPLAY_ACC_EVERY_N_STEPS: int
LEARNING_RATE: float
NUM_CLASSES: int
NUM_EPOCHS: int
NUM_HIDDEN_LAYER_NODES: int
NUM_INPUTS: int
all_inputs: Dict[Any, numpy.ndarray]
batch_x: Any
batch_y: Any
batches_x: Generator[Any, Any, None]
batches_y: Generator[Any, Any, None]
biases: Dict[str, Any]
csv: module
epoch: int
expected_outputs: numpy.ndarray
final_loss: Any
hidden_layer: Any
inputs: numpy.ndarray
logits_output_layer: Any
loss: Any
np: module
optimizer: Any
os: module
prediction: Any
session: Any
softmax_output_layer: Any
step: int
step_inputs: Dict[Any, nothing]
tf: Any
train_operation: Any
var_initializer: Any
weights: Dict[str, Any]
x: Any
y: Any
yo: Any

def batch(iterable, batch_size) -> Generator[Any, Any, None]: ...
def load_iris_dataset() -> Tuple[numpy.ndarray, numpy.ndarray]: ...
