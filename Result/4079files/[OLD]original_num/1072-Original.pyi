# (generated with --quick)

from typing import Any, Dict, Optional

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

class UrlDescriptor(object):
    GITHUB_LATEST_TEMPLATE: str
    _filename: Optional[str]
    _github_latest_release_url: Any
    _github_profile: Any
    _github_repo: Any
    _url: str
    github_profile: str
    github_repo: Any
    has_filename: bool
    is_github_repo_url: bool
    url: Any
    def __init__(self, url: str) -> None: ...
    def _parse_github_repo_url(self) -> bool: ...
    def get_github_package_url(self) -> Optional[str]: ...
    def parse_url(self) -> None: ...

class UrlDownloader(object):
    _current_url_desc: Any
    _download_path: Any
    current_url_descriptor: Any
    download_path: Any
    def __init__(self, url_descriptor: Optional[UrlDescriptor] = ...) -> None: ...
    @staticmethod
    def download_file(url: str, download_path: pathlib.Path) -> bool: ...
    def download_from_url(self, url: str, download_path: pathlib.Path) -> bool: ...
    def download_from_url_descriptor(self, url_descriptor: Optional[UrlDescriptor] = ..., download_path: Optional[pathlib.Path] = ...) -> bool: ...
    def download_latest_github_release(self, url: Optional[str] = ..., download_path: Optional[pathlib.Path] = ...) -> Optional[pathlib.Path]: ...
    def extract(self, package_path: Optional[pathlib.Path] = ..., extract_path: Optional[pathlib.Path] = ..., password: Optional[str] = ...) -> bool: ...
    @staticmethod
    def is_zip_file(file_path: pathlib.Path) -> bool: ...
    @staticmethod
    def is_zipped_dir(file_path: pathlib.Path, password: Optional[str] = ...) -> bool: ...
    @staticmethod
    def zipped_dir_name(file_path: pathlib.Path, pwd: Optional[str] = ...) -> Optional[pathlib.Path]: ...

def banner_execute() -> pathlib.Path: ...
def copy_to_dir(source_dir: pathlib.Path, dest_dir: pathlib.Path) -> bool: ...
def main(args) -> int: ...
