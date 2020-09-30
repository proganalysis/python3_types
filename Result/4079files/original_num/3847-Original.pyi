# (generated with --quick)

import collections
import json.encoder
from typing import Any, Type

OrderedDict: Type[collections.OrderedDict]
argparse: module
json: module
os: module
pickle: module
shelve: module
sqlite3: module
sys: module

class DumpJSONEncoder(json.encoder.JSONEncoder):
    __doc__: str

def dump_json(o) -> None: ...
def dump_tagged_yaml(o) -> None: ...
def dump_yaml(o) -> None: ...
def get_shelve_data(filename) -> collections.OrderedDict: ...
def get_sqlite_data(filename) -> collections.OrderedDict[str, collections.OrderedDict[str, Any]]: ...
def main() -> None: ...
