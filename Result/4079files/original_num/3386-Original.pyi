# (generated with --quick)

from typing import Any, Tuple, Type
import universe.package

Version: Type[universe.package.Version]
logger: logging.Logger
logging: module
os: module
random: module
string: module
sys: module
time: module
universe: module

class AWSPublisher(object):
    _artifact_paths: list
    _dry_run: str
    _http_directory_url: Any
    _input_dir_path: Any
    _pkg_name: Any
    _pkg_version: Any
    _universe_url_prefix: str
    _uploader: Any
    def __init__(self, package_name, package_version, input_dir_path, artifact_paths) -> None: ...
    def _spam_universe_url(self, universe_url) -> None: ...
    def upload(self) -> str: ...

def main(argv) -> int: ...
def print_help(argv) -> None: ...
def s3_urls_from_env(package_name) -> Tuple[str, str]: ...
