from typing import Any

__all__: Any
WIN_ALLOW_CROSS_ARCH: bool

def which(program: Any): ...
def is_exe(path: Any): ...
def _get_path_list(): ...
def find_exe(program: Any): ...
def get_path_list(): ...
get_path_list = _get_path_list

def main() -> None: ...