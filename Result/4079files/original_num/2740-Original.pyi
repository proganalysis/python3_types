# (generated with --quick)

import pathlib
import requests.models
from typing import Any, Dict, List, Set, Type

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
    def decorate_parser(self, parser: argparse.ArgumentParser) -> None: ...
    def run(self, args: argparse.Namespace) -> None: ...

class DownloadStats:
    downloaded: int
    errors: list
    processed: int
    skipped: int
    total: int
    def __init__(self, total: int = ..., downloaded: int = ..., errors: List[str] = ...) -> None: ...

class LinkScanResult:
    document_urls: set
    errors: list
    linkings: Dict[Any, set]
    media_urls: set
    total: int
    def __init__(self, errors: List[str] = ..., document_urls: Set[str] = ..., media_urls: Set[str] = ..., linkings: Dict[str, Set[str]] = ...) -> None: ...

class ProbeResult:
    child_urls: Set[str]
    is_media: bool
    url: str
    def __init__(self, url: str, is_media: bool, child_urls: Set[str] = ...) -> None: ...

def _collect_links(response: requests.models.Response) -> Set[str]: ...
def _download_media(args: argparse.Namespace, link_scan_result: LinkScanResult, stats: DownloadStats) -> None: ...
def _download_url(url: str, history, args: argparse.Namespace, link_scan_result: LinkScanResult) -> pathlib.Path: ...
def _get_target_path(url: str, args: argparse.Namespace, link_scan_result: LinkScanResult) -> pathlib.Path: ...
def _link_scan(args: argparse.Namespace, result: LinkScanResult) -> None: ...
def _probe_url(url: str, history) -> ProbeResult: ...
