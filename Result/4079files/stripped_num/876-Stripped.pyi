# (generated with --quick)

from typing import Any, Optional, TypeVar

Logger: Any
logger: Any
os: module
requests: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T0 = TypeVar('_T0')

class API(object):
    _scheduler_url: Any
    def __init__(self, scheduler_url) -> None: ...
    def _url(self, path: _T0) -> Any: ...

class Buckets(API):
    _scheduler_url: Any
    def create(self, project_id, exist_ok = ...) -> None: ...

class Client(object):
    buckets: Buckets
    projects: Projects
    queues: Queues
    worker: Workers
    def __init__(self, scheduler_url) -> None: ...

class HTTPError(Exception):
    __doc__: str
    message: Any
    status: Any
    def __init__(self, status, message) -> None: ...

class Projects(API):
    _scheduler_url: Any
    def create(self, name) -> Any: ...

class Queues(API):
    _scheduler_url: Any
    def add_urls(self, project_id, urls, priority) -> Any: ...
    def create(self, project_id, seeders, timeout, interval, results_mode, exist_ok = ...) -> None: ...
    def pop_urls(self, worker_id, limit) -> Any: ...
    def report_error(self, project_id, url, tag) -> None: ...
    def report_finish(self, project_id, url) -> None: ...

class Workers(API):
    _scheduler_url: Any
    def create(self, name) -> Any: ...
    def patch_projects(self, worker_id, projects) -> None: ...

def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
