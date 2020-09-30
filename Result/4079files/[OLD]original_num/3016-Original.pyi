# (generated with --quick)

import functools
import multiprocessing.pool
from typing import Any, Callable, Iterable, Optional, Type

argparse: module
argparser: argparse.ArgumentParser
args: argparse.Namespace
etree: Any
glob: module
gzip: module
multiprocessing: module
os: module
p: multiprocessing.pool.Pool
parse_partial: functools.partial[nothing]
partial: Type[functools.partial]
sys: module

def Pool(processes: Optional[int] = ..., initializer: Optional[Callable] = ..., initargs: Iterable = ..., maxtasksperchild: Optional[int] = ...) -> multiprocessing.pool.Pool: ...
def parse_pubmeds(pmids: list, file: str) -> str: ...
