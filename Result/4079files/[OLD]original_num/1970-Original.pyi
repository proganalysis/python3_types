# (generated with --quick)

import keras_extensions
import read_data
from typing import Any, Callable, Dict, Optional, Tuple, Type, Union

AnyShapeEmbedding: Type[keras_extensions.AnyShapeEmbedding]
DataProcessor: Type[read_data.DataProcessor]
Dense: Any
Dropout: Any
Embedding: Any
Input: Any
LSTM: Any
MaskedFlatten: Type[keras_extensions.MaskedFlatten]
Model: Any
NUM_EPOCHS: int
PATIENCE: int
TimeDistributedRNN: Type[keras_extensions.TimeDistributedRNN]
argparse: module
load_model: Any
numpy: module
os: module
pickle: module
sys: module

class NEM:
    __doc__: str
    custom_objects: Dict[str, Union[Callable[[Any, Any], Any], Type[Union[keras_extensions.AnyShapeEmbedding, keras_extensions.MaskedFlatten, keras_extensions.TimeDistributedRNN]]]]
    data_processor: Any
    embedding_dim: Any
    model: Any
    model_prefix: str
    use_event_structure: Any
    def __init__(self, use_event_structure = ..., embedding_dim = ...) -> None: ...
    def _build_flat_model(self, inputs, pretrained_embedding = ..., tune_embedding = ...) -> Any: ...
    def _build_structured_model(self, inputs, pretrained_embedding = ..., tune_embedding = ...) -> Any: ...
    def _save_model(self, epoch: int) -> None: ...
    def _save_model_as_best(self, epoch: int) -> None: ...
    def load_model(self, epoch: Optional[int] = ...) -> None: ...
    def make_inputs(self, filename: str, for_test = ..., pad_info = ..., include_sentences_in_events = ...) -> Tuple[Any, Any]: ...
    def test_nem(self, inputs, labels, output_filename = ...) -> None: ...
    def train_nem(self, inputs, labels, pretrained_embedding_file = ..., tune_embedding = ...) -> None: ...

def f1_score(y_true, y_pred) -> Any: ...
def main() -> None: ...
def precision(y_true, y_pred) -> Any: ...
def recall(y_true, y_pred) -> Any: ...
