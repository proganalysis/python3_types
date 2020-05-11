# (generated with --quick)

import pathlib
import requests.models
from typing import Any, List, Type

BaseCommand: Any
BeautifulSoup: Any
Flow: Any
History: Any
MEDIA_EXTENSIONS: List[str]
Path: Type[pathlib.Path]
Response: Type[requests.models.Response]
T: module
argparse: module
concurrent: module
dataclasses: module
os: module
re: module
requests_with_retry: Any
tqdm: Any
urllib: module

class DownloadCommand(Any):
    name: str
    def decorate_parser(self, parser) -> None: ...
    def run(self, args) -> None: ...

class DownloadStats:
    downloaded: int
    errors: Any
    processed: Any
    skipped: Any
    total: int
    def __init__(self) -> None: ...

class LinkScanResult:
    document_urls: Any
    errors: Any
    linkings: Any
    media_urls: Any
    total: int
    def __init__(self) -> None: ...

class ProbeResult:
    child_urls: Any
    def __init__(self) -> None: ...

def _collect_links(response) -> set: ...
def _download_media(args, link_scan_result, stats) -> None: ...
def _download_url(url, history, args, link_scan_result) -> Any: ...
def _get_target_path(url, args, link_scan_result) -> Any: ...
def _link_scan(args, result) -> None: ...
def _probe_url(url, history) -> ProbeResult: ...
