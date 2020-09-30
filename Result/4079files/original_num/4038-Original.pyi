# (generated with --quick)

from typing import Any, BinaryIO, Dict, List, TextIO

adlt: str
adult_filter: bool
argparse: module
args: argparse.Namespace
download_history: BinaryIO
hashlib: module
image_md5s: Any
imghdr: module
in_progress: List[str]
inputFile: TextIO
keyword: str
os: module
output_dir: Any
output_dir_origin: Any
output_sub_dir: str
parser: argparse.ArgumentParser
pickle: module
pool_sema: threading.BoundedSemaphore
posixpath: module
re: module
signal: module
socket: module
threading: module
time: module
tried_urls: Any
urllib: module
urlopenheader: Dict[str, str]

def backup_history(*args) -> None: ...
def download(pool_sema: threading.Semaphore, url: str, output_dir: str) -> None: ...
def fetch_images_from_keyword(pool_sema: threading.Semaphore, keyword: str, output_dir: str, filters: str, limit: int) -> None: ...
