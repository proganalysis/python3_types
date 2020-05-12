# (generated with --quick)

import __future__
from typing import Any, Dict, Tuple

BTVERSION: Tuple[int, ...]
DATASETS: Dict[str, str]
absolute_import: __future__._Feature
argparse: module
bt: Any
datetime: module
division: __future__._Feature
print_function: __future__._Feature
random: module
unicode_literals: __future__._Feature

class FixedPerc(Any):
    __doc__: str
    params: Tuple[Tuple[str, float]]
    def _getsizing(self, comminfo, cash, data, isbuy) -> Any: ...

class TheStrategy(Any):
    __doc__: str
    atr: Any
    macd: Any
    mcross: Any
    order: Any
    params: Tuple[Tuple[str, int], Tuple[str, int], Tuple[str, int], Tuple[str, int], Tuple[str, float], Tuple[str, int], Tuple[str, int]]
    pstop: Any
    sma: Any
    smadir: Any
    def __init__(self) -> None: ...
    def next(self) -> None: ...
    def notify_order(self, order) -> None: ...
    def start(self) -> None: ...

def parse_args(pargs = ...) -> argparse.Namespace: ...
def runstrat(args = ...) -> None: ...
