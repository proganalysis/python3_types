# (generated with --quick)

from typing import Any, Callable, Generator

_region: Callable[..., contextlib._GeneratorContextManager]
aws: Any
boto3: Any
contextlib: module
is_cli: bool
logging: module
mock: module
os: module
shell: Any
sys: module
util: Any
uuid: module

def _client() -> Any: ...
def _resource() -> Any: ...
def add_script(cluster_id, schema_file, script_file) -> None: ...
def add_step(cluster_id, name, *args) -> None: ...
def describe(cluster_id) -> None: ...
def emacs(path, cluster_id) -> None: ...
def instances(cluster_id) -> Any: ...
def ls(state = ...) -> Generator[str, Any, None]: ...
def main() -> None: ...
def master_instance_id(cluster_id) -> Any: ...
def new(name, *tags, application = ..., auto_shutdown = ..., release_label = ..., master_type = ..., slave_type = ..., slave_count = ..., spot = ..., spot_days = ..., key = ..., sg_master = ..., sg_slave = ..., vpc = ..., subnet = ..., job_flow_role = ..., service_role = ...) -> Any: ...
def pull(src, dst, cluster_id) -> None: ...
def push(src, dst, cluster_id) -> None: ...
def rm(*cluster_ids) -> None: ...
def scp(src, dst, cluster_id) -> None: ...
def ssh(cluster_id) -> None: ...
def wait(cluster_id, state = ...) -> None: ...