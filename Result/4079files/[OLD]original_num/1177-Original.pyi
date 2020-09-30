# (generated with --quick)

from typing import Any, Optional

algobroker: module
my_path: Any
pprint: module
qm: StrategyXbtClose
time: module

class StrategyXbtClose(algobroker.Strategy):
    active: bool
    exchange: str
    range: Any
    xbt_current_price: Optional[float]
    xbt_initial_price: Any
    def __init__(self) -> None: ...
    def process_control(self, data) -> None: ...
    def process_data(self, data) -> None: ...
    def send_cancel(self) -> None: ...
