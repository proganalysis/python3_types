import json
from typing import Any

class DumpJSONEncoder(json.JSONEncoder):
    def default(self, o: Any): ...

def dump_json(o: Any) -> None: ...
def dump_yaml(o: Any) -> None: ...
def dump_tagged_yaml(o: Any) -> None: ...
def get_sqlite_data(filename: Any): ...
def get_shelve_data(filename: Any): ...
def main() -> None: ...
