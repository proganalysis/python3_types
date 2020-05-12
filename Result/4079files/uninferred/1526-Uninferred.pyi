from pyxb.utils.domutils import *
import argparse
from typing import Any

_curdir: Any
failing_tests: Any

def to_json(infile: str, outfile: str, opts: Any) -> bool: ...
def compare_output(opts: argparse.Namespace, dict_schema: dict, outfile: str) -> bool: ...

ignore_order: bool

def compare_filter(kv1: Tuple[str, object], kv2: Tuple[str, object]) -> bool: ...
def main(argv: list) -> Any: ...
