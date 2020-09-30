# (generated with --quick)

from typing import List, Optional, Tuple

datetime: module

class AFKChecker:
    _intervals: List[Tuple[datetime.date, datetime.date]]
    def __init__(self, intervals = ...) -> None: ...
    def get_afk_end(self, today = ...) -> Optional[datetime.date]: ...
