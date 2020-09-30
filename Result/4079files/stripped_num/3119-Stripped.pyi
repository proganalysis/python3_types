# (generated with --quick)

import requests.models
from typing import Any, BinaryIO, Match, NoReturn, Optional, Tuple

BeautifulSoup: Any
Logger: Any
REQUESTS_TIMEOUT: int
Video_Containers: Any
cookies_raw2jar: Any
db: Any
descr: Any
os: module
re: module
requests: module
search_ptn: Any
setting: Any
tc: Any
time: module

class Site(object):
    _ASSIST_DELAY_TIME: Any
    _ASSIST_ONLY: Any
    _EXTEND_DESCR_BEFORE: Any
    _EXTEND_DESCR_CLONEINFO: Any
    _EXTEND_DESCR_MEDIAINFO: Any
    _EXTEND_DESCR_THUMBNAILS: Any
    cookies: Any
    db_column: str
    encode: str
    name: Any
    status: Any
    suspended: int
    url_host: str
    def __init__(self, status, cookies, **kwargs) -> None: ...
    def _assist_delay(self) -> None: ...
    @staticmethod
    def _get_torrent(torrent) -> Any: ...
    def _get_torrent_ptn(self, torrent) -> Optional[Match]: ...
    @staticmethod
    def _post_torrent_file_tuple(torrent) -> Tuple[Any, BinaryIO, str]: ...
    def enhance_descr(self, torrent, descr_text, clone_id) -> Any: ...
    def get_data(self, url, params = ..., bs = ..., json = ..., **kwargs) -> Any: ...
    def online_check(self) -> bool: ...
    def post_data(self, url, params = ..., **kwargs) -> requests.models.Response: ...
    def session_check(self) -> NoReturn: ...
    def torrent_feed(self, torrent) -> None: ...
    def torrent_reseed(self, torrent) -> NoReturn: ...
