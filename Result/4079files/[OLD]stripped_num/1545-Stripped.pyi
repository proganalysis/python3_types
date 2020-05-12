# (generated with --quick)

import json.encoder
from typing import Any, List, Pattern

Key: Any
MOVIE_CODE_PATTERN: Pattern[str]
arrow: Any
boto3: Any
decimal: module
json: module
logger: logging.Logger
logging: module
re: module

class DecimalEncoder(json.encoder.JSONEncoder): ...

class ScheduleInfo:
    created_at: Any
    date: Any
    id: Any
    movie_code: Any
    raw_data: str
    theater_code: Any
    time: Any
    def __init__(self, schedule_id, raw_data, theater_code, date, movie_code, time, created_at = ...) -> None: ...
    def __repr__(self) -> Any: ...
    def is_imax_schedule(self) -> bool: ...
    def is_valid(self) -> bool: ...

def create_schedule_info(theater_code, date, raw_data) -> ScheduleInfo: ...
def get_latest_schedule_list(minute) -> List[ScheduleInfo]: ...
def parse_schedule_info(json_str) -> ScheduleInfo: ...
def save_schedule_list(schedule_list) -> None: ...
