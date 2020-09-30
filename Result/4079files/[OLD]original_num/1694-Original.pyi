# (generated with --quick)

import __future__
import collections
import typing
from typing import Any, Dict, IO, List, Optional, Tuple, Type, Union

Counter: Type[typing.Counter]
argparse: module
args: argparse.Namespace
big_stats: Any
changes: List[Tuple[Any, Tuple[str, ...], Any, Any]]
codecs: module
copy: module
defaultdict: Type[collections.defaultdict]
i: int
indices: collections.defaultdict
most_frequent: Any
parser: argparse.ArgumentParser
re: module
sorted_vocab: list
stats: Any
sys: module
threshold: Any
unicode_literals: __future__._Feature
vocab: Dict[tuple, int]

def create_parser() -> argparse.ArgumentParser: ...
def get_pair_statistics(vocab) -> Tuple[collections.defaultdict[Tuple[Any, Any], Any], collections.defaultdict[Tuple[Any, Any], Any]]: ...
def get_vocabulary(fobj) -> typing.Counter: ...
def open(file: Union[_PathLike, bytes, int, str], mode: str = ..., buffering: int = ..., encoding: Optional[str] = ..., errors: Optional[str] = ..., newline: Optional[str] = ..., closefd: bool = ...) -> IO: ...
def prune_stats(stats, big_stats, threshold) -> None: ...
def replace_pair(pair, vocab, indices) -> List[Tuple[Any, Tuple[str, ...], Any, Any]]: ...
def update_pair_statistics(pair, changed, stats, indices) -> None: ...
