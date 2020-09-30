import struct
import termios
import fcntl
import logging
import ctypes
import os
from functools import wraps


def set_size(fd, row, col, xpix=0, ypix=0):
    winsize = struct.pack("HHHH", row, col, xpix, ypix)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, winsize)


def get_size(fd):
    data = bytearray(8)
    fcntl.ioctl(fd, termios.TIOCGWINSZ, data, True)
    return struct.unpack("HHHH", data)


STDIN = 0

CLONE_NEWNS = 0x00020000
CLONE_NEWUTS = 0x04000000
CLONE_NEWIPC = 0x08000000
CLONE_NEWUSER = 0x10000000
CLONE_NEWPID = 0x20000000
CLONE_NEWNET = 0x40000000
CLONE_NEWCGROUP = 0x02000000  # from include/uapi/linux/sched.h in Linux source code.

MS_RDONLY = 1
MS_NOSUID = 2
MS_NODEV = 4
MS_NOEXEC = 8
MS_BIND = 4096
MS_REC = 16384
MS_PRIVATE = 262144
MS_STRICTATIME = 16777216

MNT_FORCE = 1
MNT_DETACH = 2
MNT_EXPIRE = 4
UMOUNT_NOFOLLOW = 8

_libc = ctypes.CDLL("libc.so.6", use_errno=True)


def require_root(fn):
    @wraps(fn)
    def wrapper(*kargs, **kwargs):
        if os.geteuid() != 0:
            raise Exception("This operation requires root permission")
        return fn(*kargs, **kwargs)

    return wrapper


def sys_unshare(flags):
    if _libc.unshare(flags) != 0:
        raise OSError(ctypes.get_errno(), os.strerror(ctypes.get_errno()))


@require_root
def sys_mount(*kargs):
    logging.debug(repr(kargs))
    kargs = [(karg.encode("utf-8") if isinstance(karg, str) else karg) for karg in kargs]
    if _libc.mount(*kargs) != 0:
        raise OSError(ctypes.get_errno(), os.strerror(ctypes.get_errno()))


@require_root
def sys_umount(target, flags=0):
    logging.debug(repr(target))
    target = target.encode("utf-8")
    if _libc.umount2(target, flags) != 0:
        raise OSError(ctypes.get_errno(), os.strerror(ctypes.get_errno()))


@require_root
def sethostname(hostname: str):
    cstr = hostname.encode("utf-8")
    if _libc.sethostname(cstr, len(cstr)) != 0:
        raise OSError(ctypes.get_errno(), os.strerror(ctypes.get_errno()))


class Pipe:
    """Inheritable pipes for IPC"""

    def __init__(self):
        self.r, self.w = os.pipe()
        os.set_inheritable(self.r, True)
        os.set_inheritable(self.w, True)

    def close_read(self):
        os.close(self.r)

    def close_write(self):
        os.close(self.w)

    def read(self, n):
        return os.read(self.r, n)

    def write(self, bs):
        os.write(self.w, bs)
