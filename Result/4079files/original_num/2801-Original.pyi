# (generated with --quick)

import contextlib
import greenstalk
from typing import Any, Callable, Iterator, List, Type, TypeVar

BuriedError: Type[greenstalk.BuriedError]
Client: Type[greenstalk.Client]
DEFAULT_PRIORITY: int
DEFAULT_TTR: int
DeadlineSoonError: Type[greenstalk.DeadlineSoonError]
JobTooBigError: Type[greenstalk.JobTooBigError]
NotFoundError: Type[greenstalk.NotFoundError]
NotIgnoredError: Type[greenstalk.NotIgnoredError]
PORT: int
TimedOutError: Type[greenstalk.TimedOutError]
UnknownResponseError: Type[greenstalk.UnknownResponseError]
assert_seconds: Callable[..., contextlib._GeneratorContextManager[None]]
datetime: Type[datetime.datetime]
os: module
pytest: Any
subprocess: module
test_basic_usage: Any
test_binary_jobs: Any
test_delays: Any
test_delete_job_reserved_by_other: Any
test_initialize_watch_multiple: Any
test_initialize_with_tubes: Any
test_job_not_found: Any
test_kick: Any
test_kick_job: Any
test_max_job_size: Any
test_not_ignored: Any
test_pause_tube: Any
test_peek: Any
test_peek_buried: Any
test_peek_buried_not_found: Any
test_peek_delayed: Any
test_peek_delayed_not_found: Any
test_peek_not_found: Any
test_peek_ready: Any
test_peek_ready_not_found: Any
test_put_priority: Any
test_reserve_raises_on_timeout: Any
test_stats: Any
test_stats_job: Any
test_stats_tube: Any
test_ttr: Any
test_tubes: Any
test_using: Any
test_watching: Any
time: module
timedelta: Type[datetime.timedelta]

_T = TypeVar('_T')

def _parse_chunk(data: bytes, size: int) -> bytes: ...
def _parse_response(line: bytes, expected: bytes) -> List[bytes]: ...
def contextmanager(func: Callable[..., Iterator[_T]]) -> Callable[..., contextlib._GeneratorContextManager[_T]]: ...
def test_buried_error_with_id() -> None: ...
def test_buried_error_without_id() -> None: ...
def test_chunk_unexpected_eof() -> None: ...
def test_response_missing_crlf() -> None: ...
def test_str_body_no_encoding() -> None: ...
def test_unexpected_eof() -> None: ...
def test_unknown_response_error() -> None: ...
def with_beanstalkd(**kwargs) -> Callable: ...
