# (generated with --quick)

import collections
import typing
from typing import Any, Tuple, Type

Counter: Type[typing.Counter]
History: Any
Twython: Any
arrow: Any
defaultdict: Type[collections.defaultdict]
get_history_list: Any
get_latest_schedule_list: Any
get_movie_info: Any
logger: logging.Logger
logging: module
os: module
save_history_list: Any

def get_detection_list(schedule_list, history_list, condition) -> list: ...
def get_latest_raw_data() -> list: ...
def get_unique_raw_data(schedule_list) -> list: ...
def report(theater_code, message) -> Tuple[bool, Any]: ...
def report_initial_detection(schedule_list, detection_list) -> None: ...
def report_solid_detection(schedule_list, detection_list) -> None: ...
def reporter_lambda_handler(event, context) -> str: ...
