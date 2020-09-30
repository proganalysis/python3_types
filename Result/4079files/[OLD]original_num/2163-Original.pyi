# (generated with --quick)

import ctypes
import enum
import posix
from typing import Optional, Tuple, Type, Union

CDLL: Type[ctypes.CDLL]
ENOSYS: int
EPERM: int
Enum: Type[enum.Enum]
__all__: Tuple[str, str]
c_char: Type[ctypes.c_char]
c_long: Type[ctypes.c_long]

class SyscallStatus(enum.Enum):
    BLOCKED: str
    MISSING: str
    SUPPORTED: str
    __doc__: str

def create_string_buffer(init_or_size: Union[bytes, int], size: Optional[int] = ...) -> ctypes.Array[ctypes.c_char]: ...
def evaluate_statx_support() -> SyscallStatus: ...
def find_library(name: str) -> Optional[str]: ...
def get_errno() -> int: ...
def main() -> None: ...
def uname() -> posix.uname_result: ...
