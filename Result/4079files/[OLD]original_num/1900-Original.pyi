# (generated with --quick)

import pathlib
from typing import Any, Dict, List, Type

Path: Type[pathlib.Path]
architectures: List[str]
argparse: module
cmake_generator_lookup: Dict[int, str]
conan_api: Any
conan_arch_map: Dict[str, str]
openrw_path: pathlib.Path
platform: module
subprocess: module
sys: module

def create_solution(path, vs_version, arch) -> None: ...
def main() -> None: ...
def to_cmake_generator(vs_version, arch) -> str: ...
