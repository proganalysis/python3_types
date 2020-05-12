# (generated with --quick)

from typing import Any, Dict

DirectoryListProcessor: Any
ShExSchema: Any
_curdir: str
argparse: module
dict_compare: Any
failing_tests: Dict[str, str]
ignore_order: Any
json: module
os: module
re: module
sys: module

def __getattr__(name) -> Any: ...
def compare_filter(kv1, kv2) -> bool: ...
def compare_output(opts: argparse.Namespace, dict_schema: dict, outfile: str) -> bool: ...
def main(argv: list) -> None: ...
def to_json(infile: str, outfile: str, opts) -> bool: ...
