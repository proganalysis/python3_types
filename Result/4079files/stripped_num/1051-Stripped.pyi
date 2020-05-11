# (generated with --quick)

import __future__
import itertools
from typing import Any, Dict, List, Type

C0: str
CHILD_EDGE: str
CONFIG_DECODER: List[str]
CONFIG_DECODER_INFER: List[str]
CONFIG_ENCODER: List[str]
CONFIG_GENERAL: List[str]
SIBLING_EDGE: str
UNK: str
argparse: module
bayou: Any
chain: Type[itertools.chain]
json: module
print_function: __future__._Feature
random: module
re: module
tf: Any

def dump_config(config) -> Dict[str, Any]: ...
def length(tensor) -> Any: ...
def read_config(js, save_dir, infer = ...) -> argparse.Namespace: ...
def split_camel(s) -> List[str]: ...
