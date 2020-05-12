# (generated with --quick)

import pathlib
from typing import Any, Optional, Type

GooglePhotosMedia: Any
GooglePhotosRow: Any
LocalData: Any
LocalFilesMedia: Any
Path: Type[pathlib.Path]
RestClient: Any
Utils: Any
datetime: Type[datetime.datetime]
log: logging.Logger
logging: module

class GooglePhotosIndex(object):
    PAGE_SIZE: int
    _api: Any
    _db: Any
    _media_folder: pathlib.Path
    _root_folder: pathlib.Path
    _use_flat_path: bool
    end_date: None
    favourites: bool
    files_index_skipped: int
    files_indexed: int
    include_video: bool
    latest_download: Any
    rescan: bool
    start_date: None
    def __init__(self, api, root_folder: pathlib.Path, db, photos_path: pathlib.Path, use_flat_path: bool = ...) -> None: ...
    def check_for_removed(self) -> None: ...
    def check_for_removed_in_folder(self, folder: pathlib.Path) -> None: ...
    def get_extra_meta(self) -> None: ...
    def index_photos_media(self) -> bool: ...
    def search_media(self, page_token: Optional[int] = ..., start_date: Optional[datetime.datetime] = ..., end_date: Optional[datetime.datetime] = ..., do_video: bool = ..., favourites: bool = ...) -> dict: ...
    def write_media_index(self, media, update: bool = ...) -> None: ...
