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
    def __init__(self, link: str, content: str, password: str, lang: str) -> None: ...
    def get_post(self, uid: str) -> None: ...
    def post_contribution(self) -> str: ...
