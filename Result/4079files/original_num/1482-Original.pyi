# (generated with --quick)

from typing import Any, Optional, Type

datetime: Type[datetime.datetime]

class JsonPage:
    __doc__: str
    js: Any
    def __init__(self, resp) -> None: ...
    def caption(self, post_num) -> Any: ...
    def carousel_media(self, post_num) -> str: ...
    @staticmethod
    def clean_img_url(img_url) -> Any: ...
    def code(self, post_num) -> Any: ...
    def date(self, post_num) -> str: ...
    def end_cursor(self, post_num) -> Any: ...
    def likes(self, post_num) -> Any: ...
    def location(self, post_num) -> Any: ...
    def media(self, post_num) -> Any: ...
    def more_available(self) -> Any: ...
    def num_posts(self) -> int: ...
    def post_type(self, post_num) -> Any: ...
    def private_user(self, post_counter) -> Optional[bool]: ...