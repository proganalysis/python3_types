# (generated with --quick)

from typing import Any, List

re: module
requests: module

class s3_scanner:
    fingerprints: List[str]
    host: Any
    results: str
    temp: list
    totalresults: str
    def __init__(self, host) -> None: ...
    def _s3_scanner__check_http(self, bucket_url) -> None: ...
    def do_s3(self) -> None: ...
    def process(self) -> None: ...
