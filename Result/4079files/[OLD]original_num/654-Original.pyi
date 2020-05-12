# (generated with --quick)

import argparse
from typing import Any, Type, TypeVar, Union

ArgumentParser: Type[argparse.ArgumentParser]
Fastafile: Any
NormalizedLocus: Any
VariantFile: Any
match_database: Any
match_database2: Any
match_replicates: Any
records_by_chromosome: Any
sort_almost_sorted: Any
sys: module

AnyStr = TypeVar('AnyStr', str, bytes)

def add_common_args(parser) -> None: ...
def arg_parser() -> argparse.ArgumentParser: ...
def expanduser(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def main() -> None: ...
def normalize(args) -> None: ...
def run_vgraph(parser, args) -> None: ...
def tryint(s) -> int: ...
