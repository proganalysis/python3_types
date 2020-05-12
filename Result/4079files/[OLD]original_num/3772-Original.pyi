# (generated with --quick)

from typing import Any, Dict, Generator, List, Pattern, Tuple

CAMPI_EXCLUDE: List[str]
FormRequest: Any
Request: Any
Response: Any
SEMESTER: str
Subject: Any
TIMES: List[str]
collections: module
os: module
re: module
scrapy: Any

class CagrSpider(Any):
    allowed_domains: List[str]
    campi_names: collections.OrderedDict
    campus: tuple
    index: Any
    name: str
    subject: Dict[str, Any]
    table_url: str
    time_regex: Pattern[str]
    def make_requests_from_index(self, page) -> Any: ...
    def parse(self, res) -> Generator[Any, Any, None]: ...
    def start_requests(self) -> Tuple[Any]: ...
