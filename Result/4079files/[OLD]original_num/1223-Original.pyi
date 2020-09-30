# (generated with --quick)

import __future__
from typing import Any, Dict

bowerutil: module
collections: module
glob: module
hashlib: module
json: module
optparse: module
os: module
package_licenses: Dict[str, str]
print_function: __future__._Feature
subprocess: module
sys: module
tempfile: module

def bower_command(args) -> list: ...
def build_bower_json(version_targets, seeds) -> str: ...
def decode(input) -> Any: ...
def dump_build(data, seeds, out) -> None: ...
def dump_workspace(data, seeds, out) -> None: ...
def interpret_bower_json(seeds, ws_out, build_out) -> None: ...
def main(args) -> None: ...
