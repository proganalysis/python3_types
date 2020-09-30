# (generated with --quick)

import datetime
import requests.exceptions
from typing import Any, Type

ConversionApiClient: Any
Export: Any
HTTPError: Type[requests.exceptions.HTTPError]
get_cached_or_set: Any
logger: logging.Logger
logging: module
requests: module
status: Any
timedelta: Type[datetime.timedelta]

class ExportUpdaterMiddleware(object):
    def process_request(self, request) -> None: ...

def _log_cache_hit(cached_value, export, **_) -> None: ...
def _log_cache_miss(export) -> None: ...
def handle_unsent_exports(user) -> None: ...
def update_export(export, *, request) -> Any: ...
def update_export_if_stale(export, *, request) -> None: ...
def update_exports_of_request_user(request) -> None: ...
