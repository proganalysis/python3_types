# (generated with --quick)

import __future__
from typing import Any, Dict, List, Tuple

_BUCKET_FEATURE_KEYS: List[str]
_CATEGORICAL_FEATURE_KEYS: List[str]
_DENSE_FLOAT_FEATURE_KEYS: List[str]
_FARE_KEY: str
_FEATURE_BUCKET_COUNT: int
_LABEL_KEY: str
_MAX_CATEGORICAL_FEATURE_VALUES: List[int]
_OOV_SIZE: int
_VOCAB_FEATURE_KEYS: List[str]
_VOCAB_SIZE: int
division: __future__._Feature
metadata_io: Any
os: module
print_function: __future__._Feature
saved_transform_io: Any
schema_utils: Any
tf: Any
tfma: Any
tft: Any
transform_fn_io: Any

def _build_estimator(config, hidden_units = ..., warm_start_from = ...) -> Any: ...
def _eval_input_receiver_fn(transform_output, schema) -> Any: ...
def _example_serving_receiver_fn(transform_output, schema) -> Any: ...
def _fill_in_missing(x) -> Any: ...
def _get_raw_feature_spec(schema) -> Any: ...
def _gzip_reader_fn() -> Any: ...
def _input_fn(filenames, transform_output, batch_size = ...) -> Tuple[Any, Any]: ...
def _transformed_name(key) -> Any: ...
def _transformed_names(keys) -> list: ...
def preprocessing_fn(inputs) -> Dict[str, Any]: ...
def trainer_fn(hparams, schema) -> Dict[str, Any]: ...
