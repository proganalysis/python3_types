from itertools import chain as chain
from typing import Any

CONFIG_GENERAL: Any
CONFIG_ENCODER: Any
CONFIG_DECODER: Any
CONFIG_DECODER_INFER: Any
C0: str
UNK: str
CHILD_EDGE: str
SIBLING_EDGE: str

def length(tensor: Any): ...
def split_camel(s: Any): ...
def read_config(js: Any, save_dir: Any, infer: bool = ...): ...
def dump_config(config: Any): ...
