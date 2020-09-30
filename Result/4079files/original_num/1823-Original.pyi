# (generated with --quick)

import numpy
from typing import Any, Tuple

IPreprocessor: Any
ImageLoader: Any
LabelEncoder: Any
ModelSerializer: Any
RMSprop: Any
TrainingLogger: Any
ndarray: Any
np: module
np_utils: Any
train_test_split: Any

class ProcessingPipeline:
    __doc__: str
    font_names: Any
    label_encoder: Any
    model: Any
    model_path: None
    preprocessor: Any
    train_logger: Any
    def _ProcessingPipeline__compile_model(self) -> None: ...
    def __init__(self) -> None: ...
    def evaluate(self, y, y_pred) -> None: ...
    def load_features_and_preprocess(self, img_path: str, img_preprocessor) -> Tuple[numpy.ndarray, numpy.ndarray]: ...
    def load_model(self, model_path) -> None: ...
    def predict(self, x) -> Any: ...
    def save_model(self, model_save_path: str, include_stats = ...) -> None: ...
    def train_model(self, keras_model, x, y, epos = ..., train_ratio = ..., batch_size = ...) -> None: ...
