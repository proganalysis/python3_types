# (generated with --quick)

import collections
import neulion
from typing import Any, Generator, Iterator, NoReturn, Tuple, Type

ALL_SITE_URLS: Tuple[str, str, str, str]
BURNABY_URL: str
LANGLEY_URL: str
NeulionScraperApi: Type[neulion.NeulionScraperApi]
OrderedDict: Type[collections.OrderedDict]
SURREY_URL: str
VANCOUVER_URL: str
VCR: Any
adjust_timecodes_for_missing_segments: Any
date: Type[datetime.date]
datetime: Type[datetime.datetime]
myvcr: Any
pytest: Any
pytz: module
test_get_allowed_dates: Any
test_get_clips: Any
test_get_projects: Any
test_group_video_clips: Any
test_parse_time_range_from_url: Any
timedelta: Type[datetime.timedelta]

def adaptive_url_to_segment_urls(adaptive_url) -> Generator[str, Any, None]: ...
def calculate_timecodes(root_clip, subclips) -> collections.OrderedDict: ...
def get_all_configs() -> Iterator: ...
def get_config(config_id) -> Any: ...
def group_video_clips(clips) -> Any: ...
def parse_time_range_from_url(adaptive_url) -> Tuple[datetime.datetime, datetime.datetime, datetime.timedelta]: ...
def test_adaptive_url_to_segment_urls() -> None: ...
def test_adjust_timecodes_for_missing_segments() -> NoReturn: ...
def test_calculate_timecodes() -> None: ...
def test_load_all_configs() -> None: ...
def test_load_config() -> None: ...
