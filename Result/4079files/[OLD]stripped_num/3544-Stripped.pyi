# (generated with --quick)

import argparse
import pathlib
from typing import Any, Type

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
    def do_location(self, args) -> None: ...
    def do_sync(self, args) -> None: ...
    @classmethod
    def logging(cls, args, folder) -> None: ...
    def main(self, test_args = ...) -> None: ...
    def setup(self, args, db_path) -> None: ...
    def start(self, args) -> None: ...

def main() -> None: ...
