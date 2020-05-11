# (generated with --quick)

import argparse
from typing import Any, Callable, Optional, Tuple

DEPLOYQUEUE: str
access: module
authority: module
base64: module
command: module
configuration: Any
keys: module
main_command: Tuple[str, Callable[[list, argparse.ArgumentParser], Any]]
os: module
ssh: module
tempfile: module
time: module
util: module

def launch_dns_addon() -> None: ...
def launch_dns_monitor() -> None: ...
def launch_flannel() -> None: ...
def launch_flannel_monitor() -> None: ...
def launch_spec(spec_name, extra_kvs: Optional[dict] = ...) -> None: ...
def launch_spec_direct(spec_name) -> None: ...
def launch_user_grant() -> None: ...
