# (generated with --quick)

import threading
from typing import Any, Pattern, Tuple, Type, TypeVar

NotFound: Any
Thread: Type[threading.Thread]
imgur_url_pattern: Pattern[str]
os: module
praw: Any
re: module
requests: module
schedule: Any
shelve: module
time: module

_T1 = TypeVar('_T1')

class Scraper:
    folder: Any
    reddit: Any
    scraper_config: Any
    subreddit: Any
    def __init__(self, scraper_config, _folder, _subreddit, _tinify_key = ...) -> None: ...
    def crawl(self) -> None: ...
    def download(self, _url_list, _folder) -> int: ...
    @staticmethod
    def download_image(_folder, counter: _T1, ext, file_url, url, index = ...) -> Tuple[Any, Any, Any]: ...
    def start(self) -> None: ...
    def sub_exists(self, sub = ...) -> bool: ...
    @staticmethod
    def update() -> Any: ...

class ScraperConfig:
    client_id: Any
    client_secret: Any
    shelve_conf_path: Any
    shelve_keyword: Any
    user_agent: Any
    def __init__(self, reddit_client_id, reddit_client_secret, reddit_user_agent, shelve_conf_path, shelve_filename_keyword) -> None: ...
