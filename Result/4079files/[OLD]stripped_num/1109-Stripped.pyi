# (generated with --quick)

from typing import Any, Coroutine

AppSession: Any
BackwardDomainFilter: Any
BackwardFilenameFilter: Any
DirectoryFilter: Any
FollowFTPFilter: Any
HTTPSOnlyFilter: Any
HostnameFilter: Any
ItemTask: Any
LevelFilter: Any
ParentFilter: Any
RecursiveFilter: Any
RegexFilter: Any
SchemeFilter: Any
SpanHostsFilter: Any
TriesFilter: Any
_logger: logging.Logger
asyncio: module
gettext: module
logging: module

class URLFiltersPostURLImportSetupTask(Any):
    def process(self, session) -> Coroutine[Any, Any, None]: ...

class URLFiltersSetupTask(Any):
    @classmethod
    def _build_url_filters(cls, session) -> list: ...
    @classmethod
    def _build_url_rewriter(cls, session) -> Any: ...
    def process(self, session) -> Coroutine[Any, Any, None]: ...

def _(message: str) -> str: ...
