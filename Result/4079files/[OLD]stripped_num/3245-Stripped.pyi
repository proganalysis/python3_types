# (generated with --quick)

import asyncio.locks
from typing import Any, Coroutine, Optional

asyncio: module
checks: Any
commands: Any
discord: module
errors_logger: logging.Logger
functools: module
html: module
logging: module
sys: module
traceback: module
tweepy: Any
urllib3: module

class Twitter(Any):
    blacklisted_handles: list
    bot: Any
    handles: Any
    stream_listener: TwitterStreamListener
    task: Any
    twitter: Any
    twitter_add: Any
    twitter_remove: Any
    twitter_status: Any
    def __init__(self, bot) -> None: ...
    def cog_unload(self) -> None: ...
    def initialize_database(self) -> Coroutine[Any, Any, None]: ...
    def process_tweet_text(self, text, entities) -> Any: ...
    def start_twitter_feeds(self) -> Coroutine[Any, Any, None]: ...

class TwitterStreamListener(Any):
    blacklisted_handles: Any
    bot: Any
    feeds: Any
    reconnect_ready: asyncio.locks.Event
    reconnecting: bool
    stream: Any
    unique_feeds: set
    def __del__(self) -> None: ...
    def __init__(self, bot, blacklisted_handles = ...) -> None: ...
    def add_feed(self, channel, handle) -> Coroutine[Any, Any, None]: ...
    def on_error(self, status_code) -> bool: ...
    def on_exception(self, exception) -> None: ...
    def on_status(self, status) -> None: ...
    def remove_feed(self, channel, handle) -> Coroutine[Any, Any, None]: ...
    def start_feeds(self, *, feeds = ...) -> Coroutine[Any, Any, Optional[bool]]: ...

def setup(bot) -> None: ...
