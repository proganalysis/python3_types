# (generated with --quick)

import redis.client
from typing import Any, Optional

celery_config: Any
config: Any
datetime: module
json: module
log: Any
redis: module

class QcError(Exception):
    __doc__: str

class QcHandler(object):
    __doc__: str
    dbHandler: Any
    modules: dict
    redis: redis.client.Redis
    def __init__(self, app, dbHandler) -> None: ...
    def _updateRecordingsList(self, session_id) -> None: ...
    def getReport(self, session_id) -> Optional[dict]: ...
