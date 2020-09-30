# (generated with --quick)

from typing import Any, Coroutine, Dict

_LOGGER_DESTINATION: Any
_LOGGER_LEVEL: int
_LOG_LEVEL_DEBUG: int
_LOG_LEVEL_INFO: int
_MESSAGES_LIST: Dict[str, str]
__author__: str
__copyright__: str
__license__: str
__version__: str
_logger: None
exceptions: Any
lib: Any
logger: Any
os: module
payload_builder: Any
server: Any
uuid: module

class Backup(object):
    STORAGE_TABLE_BACKUPS: Any
    _MESSAGES_LIST: Dict[str, str]
    _MODULE_NAME: str
    _SCHEDULE_BACKUP_ON_DEMAND: str
    __doc__: str
    _backup_lib: Any
    _logger: Any
    _storage: Any
    def __init__(self, _storage) -> None: ...
    def _delete_backup_information(self, _id) -> Coroutine[Any, Any, None]: ...
    def create_backup(self) -> Coroutine[Any, Any, str]: ...
    def delete_backup(self, backup_id) -> Coroutine[Any, Any, None]: ...
    def get_all_backups(self, limit, skip, status, sort_order = ...) -> coroutine: ...
    def get_backup_details(self, backup_id) -> coroutine: ...
