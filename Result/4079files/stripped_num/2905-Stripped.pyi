# (generated with --quick)

from typing import Any, Dict, TextIO

StringsDict = Dict[str, Dict[str, str]]
StringsRow = Dict[str, str]

_cache: Dict[Any, Dict[str, Dict[str, str]]]
csv: module
f: TextIO
hearthstone_data: Any
json: module
path: str
sys: module

def load(fp) -> dict: ...
def load_globalstrings(locale = ...) -> Dict[str, Dict[str, str]]: ...
