# (generated with --quick)

import datetime
import redis.client
from typing import Any, Generator, Type, TypeVar

argparse: module
args: argparse.Namespace
date: Type[datetime.date]
get_socket_path: Any
parser: argparse.ArgumentParser
r: redis.client.Redis
redis: module
result: datetime.date
timedelta: Type[datetime.timedelta]
val: Any

_T0 = TypeVar('_T0')

def perdelta(start: _T0, end, delta) -> Generator[_T0, Any, None]: ...
