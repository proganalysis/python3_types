# (generated with --quick)

import io
import tarfile
from typing import Any, BinaryIO, Callable, Iterator, List, Optional, Pattern, Tuple, Type, TypeVar, Union
import zipfile

Arn: Type[str]
BytesIO: Type[io.BytesIO]
ClientError: Any
DIST_SUBDIR: str
EXCLUDE_REGEXES: List[Pattern[str]]
LAMBDA_NAME: str
MANAGED_POLICY_ARN: str
MQTT_OUTPUT_GZIP: str
OUTPUT_ZIP: str
ROLE_NAME: str
ROLE_POLICY_DOC: str
ROOT: str
TarFile: Type[tarfile.TarFile]
TarInfo: Type[tarfile.TarInfo]
ZIP_DEFLATED: int
ZipFile: Type[zipfile.ZipFile]
ZipInfo: Type[zipfile.ZipInfo]
argparse: module
boto3: Any
enum: module
json: module
log: logging.Logger
logging: module
path: module
re: module
sys: module

AnyStr = TypeVar('AnyStr', str, bytes)

class Commands(enum.Enum):
    AWS_DEPLOY: str
    ZIP_MQTT: str
    ZIP_SKILL: str

class Error(Exception):
    __doc__: str

def aws_upload(args: argparse.Namespace, zip_data: BinaryIO) -> None: ...
def chdir(path: Union[_PathLike, bytes, int, str]) -> None: ...
def create_lambda(role_arn: str, zip_data: BinaryIO, skill_id: str) -> str: ...
def create_mqtt_gzip(f: BinaryIO, root: str = ...) -> None: ...
def create_skill_zip() -> BinaryIO: ...
def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def isdir(path: Union[_PathLike, bytes, str]) -> bool: ...
def lambda_exists(name = ...) -> bool: ...
def main(args = ...) -> None: ...
def realpath(filename: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def set_up_role() -> str: ...
def suitable(name: str) -> bool: ...
def upload(zip: BinaryIO, name = ...) -> None: ...
def walk(top: Union[_PathLike[AnyStr], AnyStr], topdown: bool = ..., onerror: Optional[Callable[[OSError], Any]] = ..., followlinks: bool = ...) -> Iterator[Tuple[AnyStr, List[AnyStr], List[AnyStr]]]: ...
