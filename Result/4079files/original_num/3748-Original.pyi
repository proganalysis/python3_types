# (generated with --quick)

import collections
import functools
import typing
from typing import Any, Callable, Dict, List, Mapping, Optional, Tuple, Type, TypeVar

CRON_TRIGGER_FIELDS_COUNT: int
ChainMap: Type[typing.ChainMap]
CronTrigger: Any
DateTrigger: Any
IntervalTrigger: Any
NAME_INTERVAL_MAP: Dict[str, Tuple[int, int, int, int, int]]
ParsingError: Any
Trigger: Any
__all__: List[str]
_image_definition_labels_of_container: functools._lru_cache_wrapper[Dict[str, str]]
_parse_flags: functools._lru_cache_wrapper[str]
_parse_labels: functools._lru_cache_wrapper[Tuple[str, str, Mapping[str, dict]]]
all_timezones: List[str]
cerberus: Any
cfg: Any
defaultdict: Type[collections.defaultdict]
generate_id: Any
job_def_validator: JobConfigValidator
log: logging.Logger
logging: module
parse_time_from_string_with_units: Any
seconds_as_interval_tuple: Any
split_string: Any

_T = TypeVar('_T')

class JobConfigValidator(Any):
    _fill_args: Any
    def _normalize_coerce_cron(self, value: str) -> Tuple[type, Tuple[str, ...]]: ...
    def _normalize_coerce_date(self, value: str) -> Tuple[type, Tuple[str]]: ...
    def _normalize_coerce_interval(self, value: str) -> Tuple[type, Optional[Tuple[int, int, int, int, int]]]: ...
    def _normalize_coerce_timeunits(self, value: str) -> Optional[int]: ...
    def _validator_trigger(self, field, value) -> None: ...

def _parse_job_definitions(_labels: Mapping[str, str]) -> Dict[str, dict]: ...
def _parse_options(_labels: Dict[str, str]) -> Tuple[str, Optional[str]]: ...
def _parse_service_id(_labels: Dict[str, str]) -> str: ...
def labels(*args, **kwargs) -> Tuple[str, str, Mapping[str, dict]]: ...
def lru_cache(maxsize: Optional[int] = ..., typed: bool = ...) -> Callable[[Callable[..., _T]], functools._lru_cache_wrapper[_T]]: ...
