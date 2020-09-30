# (generated with --quick)

from typing import Any, List, Pattern, Type

IGNORE_ERRORS: List[int]
TWITTER_RE: Pattern[str]
bot: Any
container: APIContainer
datetime: Type[datetime.datetime]
hook: Any
html: module
random: module
re: module
set_api: Any
timeformat: Any
tweepy: Any
twitter: Any
twitter_url: Any
twuser: Any

class APIContainer:
    api: Any

def _get_conf_value(conf, field) -> Any: ...
def format_tweet(tweet, user) -> str: ...
def get_config(conn, field, default) -> Any: ...
def get_tweet_mode(conn, default = ...) -> Any: ...
def make_api() -> Any: ...
