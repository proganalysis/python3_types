# (generated with --quick)

import collections
from typing import Any, Pattern, Type

_date_reg_exp: Pattern[str]
aw_core: Any
datetime: Type[datetime.datetime]
defaultdict: Type[collections.defaultdict]
log_dir: Any
logging: module
os: module
re: module
today: datetime.datetime

def collect() -> collections.defaultdict: ...
def get_filepaths() -> list: ...
def line_age(line) -> int: ...
def main(exclude_testing: bool = ..., limit_days: int = ..., limit_lines: int = ...) -> None: ...
