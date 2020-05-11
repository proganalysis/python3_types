# (generated with --quick)

from typing import Any, Generator, List

INDEX_URL: str
Publication: Any
Request: Any
Spider: Any
datetime: module
extract_documents: Any
re: module

class SenatSpider(Any):
    name: str
    start_urls: List[str]
    def parse(self, response) -> Generator[Any, Any, None]: ...
    def parse_entry(self, response) -> Any: ...
