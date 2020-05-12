import datetime
from typing import List, Optional, Tuple

class AFKChecker:
    _intervals: List[Tuple[datetime.date, datetime.date]]
    def __init__(self, intervals: List[str]=...) -> None: ...
    def get_afk_end(self, today: Optional[datetime.date]=...) -> Optional[datetime.date]: ...
