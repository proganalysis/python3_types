# (generated with --quick)

import enum
import syscalls
from typing import Any, Callable, Iterable, List, Optional, Sequence, Tuple, Type
import uuid

CLONE_NEWCGROUP: int
CLONE_NEWIPC: int
CLONE_NEWNET: int
CLONE_NEWNS: int
CLONE_NEWPID: int
CLONE_NEWUSER: int
CLONE_NEWUTS: int
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
ctypes: module
fcntl: module
logging: module
mount: Callable
os: module
pty: module
re: module
sethostname: Callable
struct: module
subprocess: module
sys_mount: Callable
sys_umount: Callable
termios: module
traceback: module
tty: module

class Container:
    cgroup_paths: List[nothing]
    cgroup_specs: Any
    child_pid: int
    cleanup: Callable
    cmd: Any
    custom_mounts: Any
    do_mount: Callable
    do_umount: Callable
    env: Any
    flags: int
    gid_map: Any
    hostname: Any
    mountpoints: List[nothing]
    pid_namespace: Any
    root_path: Any
    start: Callable
    status: Any
    t_gid: int
    t_uid: int
    uid_map: Any
    user_namespace: Any
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, cmd, root_path, cgroup = ..., ipc = ..., mount = ..., pid = ..., net = ..., uts = ..., user = ..., uid_map = ..., gid_map = ..., hostname = ..., env = ..., cgroup_specs = ..., custom_mounts = ...) -> None: ...
    def apply_cgroups(self) -> Any: ...

class ContainerStatus(enum.Enum):
    ERROR: int
    RUNNING: int
    STOPPED: int

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
def try_unmount_all(l) -> list: ...
def uuid4() -> uuid.UUID: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
