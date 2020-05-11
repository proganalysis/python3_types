# (generated with --quick)

import enum
import namespace
import syscalls
from typing import Any, Callable, Iterable, Optional, Sequence, Tuple, Type
import uuid

CLONE_NEWCGROUP: int
CLONE_NEWIPC: int
CLONE_NEWNET: int
CLONE_NEWNS: int
CLONE_NEWPID: int
CLONE_NEWUSER: int
CLONE_NEWUTS: int
Container: Type[namespace.Container]
ContainerStatus: Type[namespace.ContainerStatus]
Enum: Type[enum.Enum]
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
Pipe: Type[syscalls.Pipe]
STDIN: int
UMOUNT_NOFOLLOW: int
add_to_cgroups: Callable
argparse: module
args: argparse.Namespace
c: namespace.Container
config: Any
ctypes: module
fcntl: module
logging: module
mount: Callable
os: module
parser: argparse.ArgumentParser
pty: module
re: module
root_path: Any
sethostname: Callable
specs: Any
struct: module
subprocess: module
sys_mount: Callable
sys_umount: Callable
termios: module
traceback: module
tty: module
yaml: module

def bind_mount(root_path, spec) -> Any: ...
def bindfs_mount(root_path, spec, uid, gid) -> Any: ...
def child(pipe1, pipe2, cmd, root_path, flags, pid, user, uid_map, gid_map, hostname, env) -> None: ...
def copy(fd1, fd2) -> Any: ...
def exec_in_new_process(fn) -> Callable: ...
def get_size(fd) -> tuple: ...
def link(parent_fd, child_fd) -> None: ...
def require_root(fn) -> Callable: ...
def select(rlist: Iterable, wlist: Iterable, xlist: Iterable, timeout: Optional[float] = ...) -> Tuple[list, list, list]: ...
def set_size(fd, row, col, xpix = ..., ypix = ...) -> None: ...
def sys_unshare(flags) -> None: ...
def translate(idx, mappings) -> Any: ...
def try_unmount_all(l) -> None: ...
def uuid4() -> uuid.UUID: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
