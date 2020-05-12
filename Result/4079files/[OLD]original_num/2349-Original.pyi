# (generated with --quick)

import collections
import enum
from typing import Any, Dict, Generator, Iterable, Tuple, Type

DIRECTORY_FLAG: str
Enum: Type[enum.Enum]
FILE_FLAG: str
FTP: Type[ftplib.FTP]
FTP_URL_TEMPLATE: str
LINK_FLAG: str
LISTING_FLAG_MAP: Dict[str, Any]
__all__: Tuple[str]
defaultdict: Type[collections.defaultdict]
deque: Type[collections.deque]
ensure_file_directory: Any
ftplib: module
os: module
shutil: module
urllib: module

class ListingType(enum.Enum):
    directory: str
    file: str
    link: str
    other: str

def directory_listing(conn: ftplib.FTP, path: str) -> Tuple[list, list]: ...
def download_ftp_url(source_url, target_uri, buffer_size = ...) -> None: ...
def ftp_listing_paths(ftpconn: ftplib.FTP, root: str) -> Iterable[str]: ...
def ftp_walk(ftpconn: ftplib.FTP, rootpath = ...) -> Generator[Any, Any, None]: ...
def parse_line(line: str, char_index = ...) -> Tuple[ListingType, str]: ...
