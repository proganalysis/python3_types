#!/usr/bin/python3

import argparse
import traceback

import yaml

from namespace import *


@require_root
def mount(fstype, source, target, flags=0, mount_options=[]):
    sys_mount(source, target, fstype, flags, ",".join(mount_options))
    return target


def try_unmount_all(l):
    for target in l:
        try:
            sys_umount(target, MNT_DETACH)
        except OSError:
            logging.error(f"Unmounting {target} failed.")
            logging.error(traceback.format_exc())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Starts a simple container.")
    parser.add_argument("path", help="Path to the container specification file", metavar="CFG")
    parser.add_argument("--verbose", "-v", help="Verbose mode", action="store_true", dest="verbose")
    args = parser.parse_args()
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG if args.verbose else logging.INFO)
    config = yaml.load(open(args.path))
    specs = config["specs"]
    root_path = specs["root_path"]
    c=Container(specs["command"].split(" "), root_path, **config["features"], uid_map=specs.get("uid_map", ""),
                gid_map=specs.get("gid_map", ""), hostname=specs.get("hostname", "CONTAINER"), env=config.get("env", {}),
                cgroup_specs=config.get("cgroups", {}),custom_mounts=config.get("mounts", []))
    c.do_mount()
    c.start()
    c.cleanup()