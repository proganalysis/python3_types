# (generated with --quick)

from typing import Any, Optional

S3_ACCESS_KEY: Optional[str]
S3_BUCKET: str
S3_DATASET_BUCKET: str
S3_SECRET_KEY: Optional[str]
boto3: Any
botocore: Any
datetime: module
glob: module
logging: module
os: module
pd: Any
zipfile: module

class FileManager:
    bucket: str
    local_dir: Any
    log: Any
    s3: Any
    def __hash__(self) -> int: ...
    def __init__(self, local_dir, log = ...) -> None: ...
    def clean_up(self) -> None: ...
    def download(self, files) -> list: ...
    def download_dataset(self, tournament, round_number) -> str: ...
    def read_csv(self, s3_file) -> Any: ...
