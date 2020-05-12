# (generated with --quick)

import multiprocessing.pool
from typing import Any, Dict, Tuple, Type

Pool: Type[multiprocessing.pool.Pool]
argparse: module
args: argparse.Namespace
chunk: Any
i: int
input_chunks: list
os: module
p: multiprocessing.pool.Pool
parser: argparse.ArgumentParser
scenes: Any
tf: Any
train_ds: list

def dedup(input_dir) -> Dict[str, Any]: ...
def parse_img(rough, clean, color) -> Tuple[Any, Any, Any, Any]: ...
def write_tf_records(data) -> None: ...
