# (generated with --quick)

from typing import Any, Type

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

def get_ddb_table(args, region) -> Any: ...
def get_edda_data(args, region) -> list: ...
def lift_data(args, region) -> None: ...
def main() -> None: ...
def parse_args() -> argparse.Namespace: ...
