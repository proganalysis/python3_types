import threading
from typing import Any

output_dir: str
adult_filter: bool
in_progress: Any
tried_urls: Any
image_md5s: Any
urlopenheader: Any

def download(pool_sema: threading.Semaphore, url: str, output_dir: str) -> Any: ...
def fetch_images_from_keyword(pool_sema: threading.Semaphore, keyword: str, output_dir: str, filters: str, limit: int) -> Any: ...
def backup_history(*args: Any) -> None: ...
