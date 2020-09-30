from typing import Any

VERSION: str
WPULL_VERSION: str
EXPIRE_TIME: Any
WPULL_EXE: Any
YOUTUBE_DL: Any
RSYNC: Any
version_integer: Any
WARC_MAX_SIZE: Any
WPULL_MONITOR_DISK: Any
WPULL_MONITOR_MEMORY: Any
RSYNC_URL: Any
REDIS_URL: Any
LOG_CHANNEL: Any
PIPELINE_CHANNEL: Any
project: Any

def wpull_version(): ...

class AcceptAny:
    def __contains__(self, item: Any): ...

DEFAULT_USER_AGENT: Any
_: Any
pipeline_id: Any
wpull_args: Any
pipeline: Any

def stop_control() -> None: ...
def status_running() -> None: ...
def status_stopping() -> None: ...
