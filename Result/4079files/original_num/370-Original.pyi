# (generated with --quick)

from typing import Any

Logger: Any
NexusPHP: Any
episode_eng2chs: Any
re: module
requests: module
title_clean: Any
ubb_clean: Any

class OurBits(Any):
    db_column: str
    url_host: str
    def data_raw2tuple(self, raw_info: dict) -> tuple: ...
    def date_raw_update(self, torrent, torrent_name_search, raw_info: dict) -> dict: ...
    def exist_torrent_title(self, tag) -> str: ...
    def torrent_clone(self, tid) -> dict: ...
