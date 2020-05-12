# (generated with --quick)

import concurrent.futures.thread
from typing import Any, Coroutine, Type

ThreadPoolExecutor: Type[concurrent.futures.thread.ThreadPoolExecutor]
asyncio: module
const: Any
executor: module
logger: logging.Logger
logging: module
mailer: module
notifier: module
routes: module
stats: module
stats_middleware: Any
status_logging_middleware: Any
translate: module
web: Any
wti: module
zendesk: module

def app(global_config, **settings) -> Any: ...
def start_http_clients(app) -> Coroutine[Any, Any, None]: ...
def stop_http_clients(app) -> Coroutine[Any, Any, None]: ...
