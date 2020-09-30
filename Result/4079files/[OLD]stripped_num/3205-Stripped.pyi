# (generated with --quick)

import dateutil.rrule
import pytz
from typing import Any, Dict, List, Type, Union

Calendar: Any
all_timezones: List[str]
date: Type[datetime.date]
datetime: Type[datetime.datetime]
get_localzone: Any
rruleset: Type[dateutil.rrule.rruleset]
rrulestr: dateutil.rrule._rrulestr
timedelta: Type[datetime.timedelta]
tz: module
tzinfo: Type[datetime.tzinfo]
utc: pytz._UTCclass

class orgEntry:
    __doc__: str
    dates: Any
    description: Any
    dtend: Any
    dtstart: Any
    duration: Any
    pbox: str
    properties: Dict[str, Any]
    rule: Any
    summary: Any
    tz: Any
    def __init__(self, event) -> None: ...
    def __str__(self) -> str: ...
    def _get_properties(self, event) -> None: ...
    def repeting_dates(self, start, end) -> str: ...

def orgDate(dt, tz) -> Any: ...
def orgDatetime(dt, tz) -> Any: ...
def org_interval(start, duration, tz) -> str: ...
def put_tz(date_time) -> Any: ...
def timezone(zone: str) -> Union[pytz._DstTzInfo, pytz._StaticTzInfo, pytz._UTCclass]: ...
