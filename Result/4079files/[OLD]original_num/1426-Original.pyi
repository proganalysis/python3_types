# (generated with --quick)

from typing import Any, List, Type

Binary: Any
ClientError: Any
Namespace: Type[argparse.Namespace]
ProfileNotFound: Any
argparse: module
boto3: Any
datetime: Type[datetime.datetime]
gzip: module
json: module
pprint: module
requests: module
sys: module

def get_ddb_table(args: argparse.Namespace, region: str) -> Any: ...
def get_edda_data(args: argparse.Namespace, region: str) -> List[dict]: ...
def lift_data(args: argparse.Namespace, region: str) -> None: ...
def main() -> None: ...
def parse_args() -> argparse.Namespace: ...
