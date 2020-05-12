import logging
import os
import pty
import re
import subprocess
import tty
from select import select
from uuid import uuid4
import traceback
from enum import Enum
from syscalls import *


def try_unmount_all(l):
    successes = []
    for target in l:
        try:
            sys_umount(target, MNT_DETACH)
        except OSError:
            logging.error(f"Unmounting {target} failed.")
            logging.error(traceback.format_exc())
        else:
            successes.append(target)
    return successes


def require_root(fn):
    @wraps(fn)
    def wrapper(*kargs, **kwargs):
        if os.geteuid() != 0:
            raise Exception("This operation requires root permission")
        return fn(*kargs, **kwargs)

    return wrapper


def translate(idx, mappings):
    for item in mappings:
        original_base, translated_base, length = [int(item) for item in re.split(" +", item)]
        if original_base <= idx <= original_base + length - 1:
            return translated_base + (idx - original_base)


def child(pipe1, pipe2, cmd, root_path, flags, pid, user, uid_map, gid_map, hostname, env):
    """
    Requires root privilege.
    User namespaces gives us a full set of caps, but that's too much of a hassle for me.
    """
    sys_unshare(flags)
    if flags & CLONE_NEWUTS and hostname:
        sethostname(hostname)
    elif hostname:
        logging.warning("UTS namespace not enabled, not setting hostname")
    logging.debug(f"Child PID: {os.getpid()}")
    if pid:  # CLONE_NEWPID is not included in flags. Also we need to mount a new procfs to reflect the newly created PID namespace.
        sys_mount("proc", os.path.join(root_path, "proc"), "proc", MS_NOSUID | MS_NOEXEC | MS_NODEV, None)
    else:
        logging.warning("PID namespace is disabled")
    if user:
        logging.debug("User namespace is enabled")
        # setgid and setuid to 'root' in the new user namespace.
        target_uid = translate(0, uid_map) or 65534
        target_gid = translate(0, gid_map) or 65534
        if target_gid == 65534 or target_uid == 65534:
            logging.warning("UID 0 and GID 0 are not mapped correctly")
        os.setgid(target_gid)
        os.setuid(target_uid)
        sys_unshare(CLONE_NEWUSER)
    # signal parent to update maps.
    pipe1.write(b' ')
    # wait for parent to update mappings.
    pipe2.read(1)
    os.chroot(root_path)
    os.chdir("/")  # per chroot(2) manpage.
    os.execvpe(cmd[0], cmd, env)


def exec_in_new_process(fn):
    @wraps(fn)
    def wrapper(*kargs, **kwargs):
        pid, master_fd = pty.fork()
        if pid == 0:
            fn(*kargs, **kwargs)
            exit(0)
        else:
            link(STDIN, master_fd)
            os.waitpid(pid, 0)

    return wrapper


@require_root
def add_to_cgroups(pid, specs):
    """Add process(represented by PID) to specified cgroups. Returns list of paths to cgroup directories."""
    uuid = str(uuid4())
    paths = []
    if "cpuset" in specs:
        os.mkdir(f"/sys/fs/cgroup/cpuset/{uuid}")
        with open(f"/sys/fs/cgroup/cpuset/{uuid}/cpuset.cpus", "w") as f:
            f.write(",".join([str(i) for i in specs["cpuset"]]))
        with open(f"/sys/fs/cgroup/cpuset/{uuid}/cpuset.mems", "w") as f:
            f.write("0")  # Do we really need to take NUMA into account?
        with open(f"/sys/fs/cgroup/cpuset/{uuid}/tasks", "w") as f:
            f.write(str(pid))
        paths.append(f"/sys/fs/cgroup/cpuset/{uuid}")
    if "memory" in specs:
        os.mkdir(f"/sys/fs/cgroup/memory/{uuid}")
        with open(f"/sys/fs/cgroup/memory/{uuid}/memory.limit_in_bytes", "w") as f:
            f.write(specs["memory"]["physical"])
        if "with_swap" in specs["memory"]:
            with open(f"/sys/fs/cgroup/memory/{uuid}/memory.memsw.limit_in_bytes", "w") as f:
                f.write(specs["memory"]["with_swap"])
        with open(f"/sys/fs/cgroup/memory/{uuid}/tasks", "w") as f:
            f.write(str(pid))
        paths.append(f"/sys/fs/cgroup/memory/{uuid}")
    return paths


def copy(fd1, fd2):
    fds = [fd1, fd2]
    while True:
        rfd = select(fds, [], [])[0]
        if fd1 in rfd:
            data = os.read(fd1, 1024)
            if not data:
                fds.remove(fd1)
            os.write(fd2, data)
        if fd2 in rfd:
            data = os.read(fd2, 1024)
            if not data:
                fds.remove(fd2)
            os.write(fd1, data)


def link(parent_fd, child_fd):
    try:
        mode = tty.tcgetattr(parent_fd)
        tty.setraw(parent_fd)
        rows, columns = get_size(parent_fd)[0:2]
        set_size(child_fd, rows, columns)
        restore = True
    except tty.error:
        restore = False
    try:
        copy(parent_fd, child_fd)
    except OSError:
        if restore:
            tty.tcsetattr(parent_fd, tty.TCSAFLUSH, mode)


def bindfs_mount(root_path, spec, uid, gid):
    cmd = ["bindfs", spec["source"], os.path.join(root_path, spec.get("target", spec["source"]).lstrip("/")), f"--force-user={uid}",
           f"--force-group={gid}", "--chown-deny", "--chgrp-deny", "--chmod-deny"]
    if spec.get("ro", False):
        cmd.append("-r")
    subprocess.check_call(cmd)
    return cmd[2]


def bind_mount(root_path, spec):
    target = os.path.join(root_path, spec.get("target", spec["source"]).lstrip("/"))
    sys_mount(spec["source"], target, None, MS_BIND, None)
    return target


@require_root
def mount(fstype, source, target, flags=0, mount_options=[]):
    sys_mount(source, target, fstype, flags, ",".join(mount_options))
    return target


class ContainerStatus(Enum):
    STOPPED = 0
    RUNNING = 1
    ERROR = 2


class Container:
    def __init__(self, cmd, root_path, cgroup=True, ipc=True, mount=True, pid=True, net=False, uts=True, user=True, uid_map=None, gid_map=None,
                 hostname="CONTAINER", env={}, cgroup_specs={}, custom_mounts=[]):
        self.flags = 0
        if cgroup:
            self.flags |= CLONE_NEWCGROUP
        if ipc:
            self.flags |= CLONE_NEWIPC
        if mount:
            self.flags |= CLONE_NEWNS
        if net:
            self.flags |= CLONE_NEWNET
        if uts:
            self.flags |= CLONE_NEWUTS
        self.cmd, self.root_path = cmd, root_path
        self.pid_namespace = pid
        self.user_namespace = user
        self.uid_map, self.gid_map = uid_map, gid_map
        self.hostname = hostname
        self.env = env
        self.mountpoints = []
        self.status = ContainerStatus.STOPPED
        self.cgroup_specs = cgroup_specs
        self.t_uid = 0
        self.t_gid = 0
        self.child_pid = 0
        self.cgroup_paths = []
        self.custom_mounts = custom_mounts

    def apply_cgroups(self):
        return add_to_cgroups(self.child_pid, self.cgroup_specs)

    @exec_in_new_process
    def start(self):
        self.status = ContainerStatus.RUNNING
        pipe1 = Pipe()
        pipe2 = Pipe()
        if self.pid_namespace:
            sys_unshare(CLONE_NEWPID)
        self.child_pid, master_fd = pty.fork()
        if self.child_pid != 0:
            self.cgroup_paths = self.apply_cgroups()
            # Wait for child to unshare user namespaces before updating relevant mappings.
            pipe1.read(1)
            if self.user_namespace:
                if self.uid_map:
                    logging.debug(f"uid_map:{repr(self.uid_map)}")
                    with open(f"/proc/{str(self.child_pid)}/uid_map", "w") as f:
                        f.write("\n".join(self.uid_map))
                if self.gid_map:
                    logging.debug(f"gid_map:{repr(self.gid_map)}")
                    with open(f"/proc/{str(self.child_pid)}/gid_map", "w") as f:
                        f.write("\n".join(self.gid_map))
                logging.debug("Parent:Maps updated")
            pipe2.write(b' ')
            link(STDIN, master_fd)
            os.waitpid(self.child_pid, 0)
            self.status = ContainerStatus.STOPPED
            sys_umount(os.path.join(self.root_path, "proc"))
        else:
            child(pipe1, pipe2, self.cmd, self.root_path, self.flags, self.pid_namespace, self.user_namespace, self.uid_map, self.gid_map,
                  self.hostname, self.env)

    @require_root
    def do_mount(self, processor=None):
        if self.user_namespace:
            self.t_uid = translate(0, self.uid_map)
            self.t_gid = translate(0, self.gid_map)
        else:
            self.t_uid = 0
            self.t_gid = 0
        mount_params_list = [
            ("sysfs", "sys", os.path.join(self.root_path, "sys"), MS_NOSUID | MS_NOEXEC | MS_NODEV | MS_RDONLY, []),
            ("devtmpfs", "udev", os.path.join(self.root_path, "dev"), MS_NOSUID, ["mode=0755"]),
            ("devpts", "devpts", os.path.join(self.root_path, "dev/pts"), MS_NOEXEC | MS_NOSUID, ["mode=0620", "gid=5"]),
            ("tmpfs", "shm", os.path.join(self.root_path, "dev/shm"), MS_NOSUID | MS_NODEV, ["mode=1777"]),
            ("tmpfs", "run", os.path.join(self.root_path, "run"), MS_NOSUID | MS_NODEV, ["mode=0755", f"uid={self.t_uid}", f"gid={self.t_gid}"]),
            ("tmpfs", "tmp", os.path.join(self.root_path, "tmp"), MS_STRICTATIME | MS_NODEV | MS_NOSUID, ["mode=1777"])
        ]
        if callable(processor):
            processor(mount_params_list)
        for mount_params in mount_params_list:
            try:
                self.mountpoints.append(mount(*mount_params))
            except OSError:
                logging.error(f"Mounting {mount_params[2]} failed.")
                logging.debug(traceback.format_exc())
                try_unmount_all([x[2] for x in mount_params_list])
                exit(1)
        for mount_spec in self.custom_mounts:
            try:
                if 'type' not in mount_spec or mount_spec['type'] == 'bind':
                    self.mountpoints.append(bind_mount(self.root_path, mount_spec))
                elif mount_spec["type"] == "bindfs":
                    self.mountpoints.append(bindfs_mount(self.root_path, mount_spec, self.t_uid, self.t_gid))
            except (OSError, subprocess.CalledProcessError, KeyError):
                logging.debug(traceback.format_exc())
                logging.debug(repr(mount_spec))
                logging.error("A binding operation failed. Quitting")
                try_unmount_all(self.mountpoints)
                self.status = ContainerStatus.ERROR
                exit(1)

    @require_root
    def do_umount(self):
        for mountpoint in try_unmount_all(reversed(self.mountpoints)):
            self.mountpoints.remove(mountpoint)
        if self.mountpoints:
            logging.error(f"Cleanup incomplete, failed to unmount {repr(self.mountpoints)}")

    @require_root
    def cleanup(self):
        self.do_umount()
        for path in self.cgroup_paths:
            os.rmdir(path)

    def __enter__(self):
        self.do_mount()
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()
