import datetime
from typing import Any, Optional, Sequence

def roundTime(dt: Optional[Any] = ..., roundTo: int = ...): ...
def filter_datetimes(datetimes: Sequence[datetime.datetime], leeway: int, target_dt: datetime.datetime) -> Any: ...
def format_dt(dt: datetime.datetime) -> Any: ...
def sort_datetimes_by_closeness_to_datetime(datetimes: Sequence[datetime.datetime], closeness_dt: datetime.datetime) -> Sequence[datetime.datetime]: ...
def difference_in_minutes(dt1: datetime.datetime, dt2: datetime.datetime) -> int: ...