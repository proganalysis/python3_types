from prawcore import NotFound as NotFound
from typing import Any, Optional

imgur_url_pattern: Any

class ScraperConfig:
    client_id: Any = ...
    client_secret: Any = ...
    user_agent: Any = ...
    shelve_conf_path: Any = ...
    shelve_keyword: Any = ...
    def __init__(self, reddit_client_id: Any, reddit_client_secret: Any, reddit_user_agent: Any, shelve_conf_path: Any, shelve_filename_keyword: Any) -> None: ...

class Scraper:
    folder: Any = ...
    subreddit: Any = ...
    scraper_config: Any = ...
    reddit: Any = ...
    def __init__(self, scraper_config: ScraperConfig, _folder: Any, _subreddit: Any, _tinify_key: Any=...) -> None: ...
    def crawl(self) -> None: ...
    def start(self) -> None: ...
    def download(self, _url_list: Any, _folder: Any): ...
    @staticmethod
    def download_image(_folder: Any, counter: Any, ext: Any, file_url: Any, url: Any, index: int = ...): ...
    def sub_exists(self, sub: Optional[Any] = ...): ...
    @staticmethod
    def update() -> None: ...