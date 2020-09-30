# (generated with --quick)

from typing import Any

db: Any
objectid: Any
post: Any

class ResponsePost(Any):
    __doc__: str
    content: Any
    id: str
    lang: Any
    limit: Any
    link: Any
    password: Any
    def __init__(self, link, content, password, lang) -> None: ...
    def get_post(self, uid) -> None: ...
    def post_contribution(self) -> str: ...
