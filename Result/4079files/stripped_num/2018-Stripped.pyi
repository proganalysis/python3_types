# (generated with --quick)

from typing import Any, Pattern, Tuple, TypeVar

Logger: Any
NexusPHP: Any
base64: module
episode_eng2chs: Any
re: module
requests: module
ubb_clean: Any

_T2 = TypeVar('_T2')

class NPUBits(Any):
    _pat_search_torrent_id: Pattern[str]
    db_column: str
    url_host: str
    def data_raw2tuple(self, raw_info) -> Tuple[Tuple[str, Any], Tuple[str, Any], Tuple[str, Any], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, str], Tuple[str, Any], Tuple[str, str], Tuple[str, str]]: ...
    def date_raw_update(self, torrent, torrent_name_search, raw_info: _T2) -> _T2: ...
    def page_search(self, key, bs = ...) -> Any: ...
    def torrent_clone(self, tid) -> Any: ...
    def torrent_thank(self, tid) -> None: ...
    @staticmethod
    def torrent_upload_err_message(post_text) -> str: ...

def string2base64(raw) -> str: ...
