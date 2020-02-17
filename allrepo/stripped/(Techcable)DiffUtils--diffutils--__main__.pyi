# (generated with --quick)

import pathlib
from typing import Any, Type

CommandError: Any
DiffEngine: Any
PatchFailedException: Any
Path: Type[pathlib.Path]
arg: Any
argh: Any
diff: Any
diffutils: Any
fix_patch: Any
generate_unified_diff: Any
os: module
parse_unified_diff: Any
patch: Any

def do_diff(engine, original, revised, output, context_size = ..., force = ...) -> bool: ...
def do_patch(patch_file, original, output, context_size = ..., force = ...) -> None: ...
def main() -> None: ...
