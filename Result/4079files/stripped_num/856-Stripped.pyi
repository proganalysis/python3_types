# (generated with --quick)

import _importlib_modulespec
import asyncio.events
from typing import Any, Callable, Coroutine, Optional, Sequence

APP_CLIENT_ID: Any
APP_CLIENT_SECRET: Any
APP_ID: Any
APP_KEY: Any
BOT_NAME: Any
CODE_SIGNING_KEY: Any
Celery: Any
GitHubAppHandler: Any
GitHubHandler: Any
REPODATA_TIMEOUT: Any
RepoData: Any
Task: Any
abc: module
aiohttp: Any
asyncio: module
capp: Any
celeryd_init: Any
install_gpg_key: Any
logger: logging.Logger
logging: module
os: module
re: module
serialization: Any
setup_logger: Any
setup_new_celery_process: Any
simplejson: module
subprocess: module

class AsyncTask(Any):
    __doc__: str
    _async_run: Optional[Callable]
    acks_late: bool
    ghapi: None
    ghappapi: Any
    loop: asyncio.events.AbstractEventLoop
    run: Any
    def async_init(self) -> Coroutine[Any, Any, None]: ...
    def async_pre_run(self, args, _kwargs) -> Coroutine[Any, Any, None]: ...
    def bind(self, app = ...) -> None: ...

def custom_dumps(string) -> str: ...
def custom_loads(string) -> Any: ...
def import_module(name: str, package: Optional[str] = ...) -> _importlib_modulespec.ModuleType: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
