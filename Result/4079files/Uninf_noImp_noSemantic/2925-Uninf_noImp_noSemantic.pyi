import tensorflow as tf
from typing import Any, Dict, Tuple

parser: Any
args: Any

def parse_img(rough: tf.Tensor, clean: tf.Tensor, color: tf.Tensor) -> Tuple[tf.Tensor, ...]: ...
def dedup(input_dir: str) -> Dict[str, Any]: ...
def write_tf_records(data: Dict[str, Any]) -> None: ...
