# (generated with --quick)

from typing import Any, Iterable, Iterator, Type
import yaml.cyaml

CLoader: Type[yaml.cyaml.CLoader]
LOG_FORMAT: str
ZK_DEFAULT_CLUSTER_TYPE: str
ZK_TOPOLOGY_DIR: str
argparse: module
glob: module
kazoo: Any
log: logging.Logger
logging: module
os: module
yaml: module

def clean(simulate: bool, zk) -> int: ...
def get_zk_cluster_locations(cluster_type: str) -> Iterator[str]: ...
def get_zk_topology(cluster_type: str, cluster_location: str) -> Iterable[str]: ...
def main() -> None: ...
def parse_args() -> argparse.Namespace: ...
