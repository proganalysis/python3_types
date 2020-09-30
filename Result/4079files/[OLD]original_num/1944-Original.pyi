# (generated with --quick)

from typing import Any, List, Optional

WETRANSFER_API_URL: str
WETRANSFER_DEFAULT_CHUNK_SIZE: int
WETRANSFER_DOWNLOAD_URL: str
WETRANSFER_FILES_URL: str
WETRANSFER_FINALIZE_MPP_URL: str
WETRANSFER_FINALIZE_URL: str
WETRANSFER_PART_PUT_URL: str
WETRANSFER_UPLOAD_EMAIL_URL: str
WETRANSFER_UPLOAD_LINK_URL: str
ap: argparse.ArgumentParser
argparse: module
args: argparse.Namespace
dp: argparse.ArgumentParser
os: module
requests: module
sp: argparse._SubParsersAction
u: Any
up: argparse.ArgumentParser
urllib: module
zlib: module

def _file_name_and_size(file: str) -> dict: ...
def _finalize_upload(transfer_id: str) -> str: ...
def _prepare_email_upload(filenames: List[str], message: str, sender: str, recipients: List[str]) -> str: ...
def _prepare_file_upload(transfer_id: str, file: str) -> str: ...
def _prepare_link_upload(filenames: List[str], message: str) -> str: ...
def _upload_chunks(transfer_id: str, file_id: str, file: str, default_chunk_size: int = ...) -> str: ...
def download(url: str) -> None: ...
def download_url(url: str) -> str: ...
def upload(files: List[str], message: str = ..., sender: Optional[str] = ..., recipients: List[str] = ...) -> str: ...
