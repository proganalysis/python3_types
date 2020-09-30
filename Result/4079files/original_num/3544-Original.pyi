# (generated with --quick)

import argparse
import pathlib
from typing import Any, Optional, Type

APP_NAME: str
AppDirs: Any
ArgumentParser: Type[argparse.ArgumentParser]
Authorize: Any
DistributionNotFound: Type[pkg_resources.DistributionNotFound]
GoogleAlbumsSync: Any
GooglePhotosDownload: Any
GooglePhotosIndex: Any
LocalData: Any
LocalFilesScan: Any
LocationUpdate: Any
Namespace: Type[argparse.Namespace]
Path: Type[pathlib.Path]
RestClient: Any
Utils: Any
__version__: str
datetime: Type[datetime.datetime]
fcntl: module
log: logging.Logger
logging: module
os: module
pkg_resources: module
sys: module

class GooglePhotosSyncMain:
    _end_date: Any
    _start_date: Any
    auth: Any
    data_store: Any
    google_albums_sync: Any
    google_photos_client: Any
    google_photos_down: Any
    google_photos_idx: Any
    local_files_scan: Any
    location_update: Any
    parser: argparse.ArgumentParser
    version_string: str
    def __init__(self) -> None: ...
    def do_location(self, args: argparse.Namespace) -> None: ...
    def do_sync(self, args: argparse.Namespace) -> None: ...
    @classmethod
    def logging(cls, args: argparse.Namespace, folder: pathlib.Path) -> None: ...
    def main(self, test_args: Optional[dict] = ...) -> None: ...
    def setup(self, args: argparse.Namespace, db_path: pathlib.Path) -> None: ...
    def start(self, args: argparse.Namespace) -> None: ...

def main() -> None: ...
