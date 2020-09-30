# (generated with --quick)

from typing import Any, Tuple

SingletonModel: Any
TelegramError: Any
URLField: Any
ValidationError: Any
bot: Any
feedparser: Any
models: Any

class Channel(Any):
    BUTTON_TYPES: Tuple[Tuple[str, str], Tuple[str, str], Tuple[str, str]]
    LINK_AND_COMMENTS_BUTTONS: str
    LINK_BUTTON: str
    NO_BUTTONS: str
    buttons_type: Any
    chat_id: Any
    identifier: Any
    linked_title: Any
    publish_picture: Any
    short_link: Any
    signature: Any
    tg_link: str
    title: Any
    username: Any
    def __str__(self) -> Any: ...
    def clean(self) -> None: ...
    def save(self, refresh_meta = ..., **kwargs) -> None: ...

class Post(Any):
    Meta: type
    comments_link: Any
    created: Any
    feed: Any
    link: Any
    pic_link: Any
    title: Any
    def __repr__(self) -> str: ...
    def __str__(self) -> Any: ...
    def validate_unique(self, exclude = ...) -> None: ...

class RssFeed(Any):
    Meta: type
    active: Any
    channel: Any
    link: Any
    link_field: Any
    title: Any
    def __str__(self) -> str: ...
    def clean(self) -> None: ...
    def save(self, update_title = ..., **kwargs) -> None: ...
