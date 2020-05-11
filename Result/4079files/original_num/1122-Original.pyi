# (generated with --quick)

from typing import Callable, Sequence

CLONE_NEWCGROUP: int
CLONE_NEWIPC: int
CLONE_NEWNET: int
CLONE_NEWNS: int
CLONE_NEWPID: int
CLONE_NEWUSER: int
CLONE_NEWUTS: int
MNT_DETACH: int
MNT_EXPIRE: int
MNT_FORCE: int
MS_BIND: int
MS_NODEV: int
MS_NOEXEC: int
MS_NOSUID: int
MS_PRIVATE: int
MS_RDONLY: int
MS_REC: int
MS_STRICTATIME: int
STDIN: int
UMOUNT_NOFOLLOW: int
_libc: ctypes.CDLL
ctypes: module
fcntl: module
logging: module
os: module
sethostname: Callable
struct: module
sys_mount: Callable
sys_umount: Callable
termios: module

class Pipe:
    __doc__: str
    r: int
    w: int
    def __init__(self) -> None: ...
    def close_read(self) -> None: ...
    def close_write(self) -> None: ...
    def read(self, n) -> bytes: ...
    def write(self, bs) -> None: ...

def get_size(fd) -> tuple: ...
def require_root(fn) -> Callable: ...
def set_size(fd, row, col, xpix = ..., ypix = ...) -> None: ...
def sys_unshare(flags) -> None: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
