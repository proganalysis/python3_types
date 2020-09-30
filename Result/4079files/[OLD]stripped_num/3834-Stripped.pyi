# (generated with --quick)

import archivebot.control
import archivebot.seesaw.tasks
import archivebot.seesaw.wpull
import distutils.version
from typing import Any, Type, Union

CheckIP: Type[archivebot.seesaw.tasks.CheckIP]
DEFAULT_USER_AGENT: str
DownloadUrlFile: Type[archivebot.seesaw.tasks.DownloadUrlFile]
EXPIRE_TIME: int
GetItemFromQueue: Type[archivebot.seesaw.tasks.GetItemFromQueue]
ItemInterpolation: Any
ItemValue: Any
LOG_CHANNEL: Any
LimitConcurrent: Any
MarkItemAsDone: Type[archivebot.seesaw.tasks.MarkItemAsDone]
MoveFiles: Type[archivebot.seesaw.tasks.MoveFiles]
PIPELINE_CHANNEL: Any
Pipeline: Any
PreparePaths: Type[archivebot.seesaw.tasks.PreparePaths]
Project: Any
REDIS_URL: str
RSYNC: Any
RSYNC_URL: str
RelabelIfAborted: Type[archivebot.seesaw.tasks.RelabelIfAborted]
RsyncUpload: Any
SetFetchDepth: Type[archivebot.seesaw.tasks.SetFetchDepth]
StartHeartbeat: Type[archivebot.seesaw.tasks.StartHeartbeat]
StopHeartbeat: Type[archivebot.seesaw.tasks.StopHeartbeat]
StrictVersion: Type[distutils.version.StrictVersion]
VERSION: str
WARC_MAX_SIZE: str
WPULL_EXE: Any
WPULL_MONITOR_DISK: str
WPULL_MONITOR_MEMORY: str
WPULL_VERSION: str
WgetDownload: Any
WpullArgs: Type[archivebot.seesaw.wpull.WpullArgs]
WriteInfo: Type[archivebot.seesaw.tasks.WriteInfo]
YOUTUBE_DL: Any
_: str
atexit: module
control: Union[module, archivebot.control.Control]
env: os._Environ[str]
extensions: module
find_executable: Any
monitoring: module
os: module
pipeline: Any
pipeline_id: str
project: Any
seesaw: Any
shared_config: module
subprocess: module
sys: module
version_integer: int
wpull_args: archivebot.seesaw.wpull.WpullArgs

class AcceptAny:
    def __contains__(self, item) -> bool: ...

def check_wpull_args(wpull_args) -> None: ...
def status_running() -> None: ...
def status_stopping() -> None: ...
def stop_control() -> None: ...
def wpull_version() -> str: ...
