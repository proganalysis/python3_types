# (generated with --quick)

import enum
from typing import Any, Type

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
    _category: Any
    _display: controller.Display
    _polling_interval: Any
    _scraper: Scraper
    _subreddit: Any
    def __init__(self, polling_interval = ..., subreddit = ..., category = ...) -> None: ...
    def _poll_titles(self, num) -> list: ...
    def start_polling(self) -> Any: ...

class Scraper:
    __doc__: str
    _reddit: Any
    def __init__(self) -> None: ...
    def scrape(self, subreddit_name = ..., category = ..., num_submissions = ...) -> Any: ...
