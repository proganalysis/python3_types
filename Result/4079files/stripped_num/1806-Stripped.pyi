# (generated with --quick)

from typing import Any, List, Pattern

demjson: Any
logging: module
re: module

class BandcampJSON:
    body: Any
    js_data: Any
    json_data: list
    regex: Pattern[str]
    target: str
    targets: List[str]
    def __init__(self, body, debugging = ...) -> None: ...
    def extract_data(self, js) -> None: ...
    def generate(self) -> list: ...
    def get_js(self) -> None: ...
    def get_pagedata(self) -> None: ...
    def js_to_json(self) -> None: ...
