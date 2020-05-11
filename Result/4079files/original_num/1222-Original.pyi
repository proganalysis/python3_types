# (generated with --quick)

import enum
from typing import Any, List, Optional, Type

Enum: Type[enum.Enum]
controller: module
praw: Any
time: module
view: RedditView

class Category(enum.Enum):
    CONROVERSIAL: str
    GILDED: str
    HOT: str
    NEW: str
    RISING: str
    TOP: str

class RedditView:
    __doc__: str
    _category: Category
    _display: controller.Display
    _polling_interval: int
    _scraper: Scraper
    _subreddit: str
    def __init__(self, polling_interval: int = ..., subreddit: str = ..., category: Category = ...) -> None: ...
    def _poll_titles(self, num: int) -> List[str]: ...
    def start_polling(self) -> None: ...

class Scraper:
    __doc__: str
    _reddit: Any
    def __init__(self) -> None: ...
    def scrape(self, subreddit_name: str = ..., category: Category = ..., num_submissions: Optional[int] = ...) -> list: ...
