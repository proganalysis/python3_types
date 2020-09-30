# (generated with --quick)

from typing import Any, Dict, Set, Tuple, Type

cau: Crawler
datetime: Type[datetime.datetime]
get_date: Type[datetime.date]
json: module
os: module
requests: module
time: module

class Crawler:
    bamboo_id: Any
    bamboo_nickname: Any
    first_date: Any
    first_day: int
    headers: Dict[str, str]
    mypath: str
    notExistDays: Set[nothing]
    def __init__(self, bamboo_tuple, first_date) -> None: ...
    def getDataWithDate(self, date, page) -> Any: ...
    def writeContent(self, post_num) -> None: ...
    def writeJSON(self, day, post_num) -> Tuple[Any, Any]: ...
