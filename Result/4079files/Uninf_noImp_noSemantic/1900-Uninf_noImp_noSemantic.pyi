from typing import Any

openrw_path: Any
cmake_generator_lookup: Any
architectures: Any
conan_arch_map: Any

def to_cmake_generator(vs_version: Any, arch: Any): ...
def create_solution(path: Any, vs_version: Any, arch: Any) -> None: ...
def main() -> None: ...
