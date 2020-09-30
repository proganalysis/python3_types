# (generated with --quick)

from typing import Any, Dict, Tuple, TypeVar

Logger: Any
NexusPHP: Any
episode_eng2chs: Any
re: module
requests: module
title_clean: Any
ubb_clean: Any

_T2 = TypeVar('_T2')

class OurBits(Any):
    db_column: str
    url_host: str
    def data_raw2tuple(self, raw_info) -> Tuple[Tuple[str, Any], ...]: ...
    def date_raw_update(self, torrent, torrent_name_search, raw_info: _T2) -> _T2: ...
    def exist_torrent_title(self, tag) -> str: ...
    def torrent_clone(self, tid) -> Dict[str, Any]: ...
