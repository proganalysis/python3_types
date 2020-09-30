# (generated with --quick)

import contextlib
from typing import Any, Tuple, Type

C: Any
ExitStack: Type[contextlib.ExitStack]
TopKLexicon: Any
argparse: module
arguments: Any
arguments_image: Any
batching: Any
check_condition: Any
determine_context: Any
extract_features_forward: Any
get_pretrained_net: Any
inference: Any
inference_image: Any
log_basic_info: Any
logger: logging.Logger
logging: module
mx: Any
os: module
output_handler: Any
read_and_translate: Any
read_feature_shape: Any
read_list_file: Any
setup_main_logger: Any
tempfile: module
utils: Any

def _extract_features(args, context) -> Tuple[str, str, tuple]: ...
def caption(args: argparse.Namespace) -> None: ...
def get_pretrained_caption_net(args: argparse.Namespace, context, image_preextracted_features: bool, features_in_memory = ...) -> Any: ...
def main() -> None: ...
