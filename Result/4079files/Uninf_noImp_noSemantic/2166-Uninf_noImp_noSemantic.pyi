from typing import Any

__all__: Any
SCRIPT_CONFIG: Any
LOG: Any
API_URL: str
DEFAULT_HEADERS: Any
API_BUSINESS: str
API_INTELLIGENT: str
API_DESIGN: str
API_FASHION: str
API_ENTERTAINMENT: str
API_CITY: str
API_GAME: str
API_LONG: str
ARTICLE_ID_SET: Any
META: Any
HTML_PARSER_NAME: str
DESC: Any

def main(start: str = ..., end: str = ..., i: str = ..., img: bool = ..., gif: bool = ..., email: bool = ..., **kw: Any) -> None: ...
def qdaily_main(start: Any, end: Any, kw: Any) -> None: ...
def parser_list(task: Any): ...
def parser_content(task: Any): ...
def resulter_content(task: Any) -> None: ...
def parser_downloader_img(task: Any): ...
def resulter_downloader_img(task: Any) -> None: ...
