# (generated with --quick)

from typing import Any, Generator, List, Type
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

def clean(simulate, zk) -> int: ...
def get_zk_cluster_locations(cluster_type) -> Generator[str, Any, None]: ...
def get_zk_topology(cluster_type, cluster_location) -> List[str]: ...
def main() -> None: ...
def parse_args() -> argparse.Namespace: ...
