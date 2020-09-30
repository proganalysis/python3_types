# (generated with --quick)

from typing import Any, Dict

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

def _file_name_and_size(file) -> Dict[str, Any]: ...
def _finalize_upload(transfer_id) -> Any: ...
def _prepare_email_upload(filenames, message, sender, recipients) -> Any: ...
def _prepare_file_upload(transfer_id, file) -> Any: ...
def _prepare_link_upload(filenames, message) -> Any: ...
def _upload_chunks(transfer_id, file_id, file, default_chunk_size = ...) -> Any: ...
def download(url) -> None: ...
def download_url(url) -> Any: ...
def upload(files, message = ..., sender = ..., recipients = ...) -> Any: ...
