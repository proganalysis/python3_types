# (generated with --quick)

from typing import Any, Dict, Optional, TypeVar

HTTP_HEADERS: Dict[str, str]
arg_parser: argparse.ArgumentParser
argparse: module
json: module
logger: logging.Logger
logging: module
os: module
parsed_args: argparse.Namespace
pathlib: module
requests: module
shutil: module
sys: module
urllib: module
zipfile: module

_T1 = TypeVar('_T1')

class UrlDescriptor(object):
    GITHUB_LATEST_TEMPLATE: str
    _filename: Optional[str]
    _github_latest_release_url: Any
    _github_profile: Any
    _github_repo: Any
    _url: Any
    github_profile: Any
    github_repo: Any
    has_filename: bool
    is_github_repo_url: bool
    url: Any
    def __init__(self, url) -> None: ...
    def _parse_github_repo_url(self) -> bool: ...
    def get_github_package_url(self) -> Any: ...
    def parse_url(self) -> None: ...

class UrlDownloader(object):
    _current_url_desc: Any
    _download_path: Any
    current_url_descriptor: Any
    download_path: Any
    def __init__(self, url_descriptor = ...) -> None: ...
    @staticmethod
    def download_file(url, download_path) -> bool: ...
    def download_from_url(self, url, download_path) -> Any: ...
    def download_from_url_descriptor(self, url_descriptor = ..., download_path = ...) -> bool: ...
    def download_latest_github_release(self, url = ..., download_path: _T1 = ...) -> Optional[_T1]: ...
    def extract(self, package_path = ..., extract_path = ..., password = ...) -> bool: ...
    @staticmethod
    def is_zip_file(file_path) -> bool: ...
    @staticmethod
    def is_zipped_dir(file_path, password = ...) -> bool: ...
    @staticmethod
    def zipped_dir_name(file_path, pwd = ...) -> Optional[str]: ...

def banner_execute() -> pathlib.Path: ...
def copy_to_dir(source_dir, dest_dir) -> Optional[bool]: ...
def main(args) -> int: ...
