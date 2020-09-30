# (generated with --quick)

import multiprocessing.pool
from typing import Any, Dict, List, Type

Pool: Type[multiprocessing.pool.Pool]
argparse: module
args: argparse.Namespace
chunk: Dict[str, Any]
i: int
input_chunks: List[Dict[str, Any]]
os: module
p: multiprocessing.pool.Pool
parser: argparse.ArgumentParser
scenes: Any
tf: Any
train_ds: List[None]

def dedup(input_dir: str) -> Dict[str, Any]: ...
def parse_img(rough, clean, color) -> tuple: ...
def write_tf_records(data: Dict[str, Any]) -> None: ...
