# (generated with --quick)

from typing import Any, Dict, Mapping, Sequence, Union

account: Any
chrono: Any
collections: module
copy: module
decimal: module
heapq: module
pig: module

class Cashflow:
    __doc__: str
    cashflow: Union[Dict[Any, list], collections.OrderedDict[Any, Sequence], Mapping[Any, Sequence]]
    pinch_points_spend: Any
    pinch_points_svg: Any
    start_date_totals: tuple
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def _events_total(self, pigs, start_date, end_date) -> None: ...
    def _locate_pinch_points(self, pinch_count) -> None: ...
    def predictor(self, accs, pigs, start_date = ..., end_date = ..., pinch_count = ...) -> None: ...
