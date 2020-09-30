from collections import namedtuple
from typing import Any

CONFLICTS: Any
types: Any

Var = namedtuple('Var', ['name', 'type', 'default', 'help', 'flags', 'filename'])
VARS: Any

def process(filename: Any, args: Any) -> None: ...
def dump(folder: Any) -> None: ...
def main() -> None: ...
