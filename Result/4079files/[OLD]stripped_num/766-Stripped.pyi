# (generated with --quick)

import contextlib
import hashlib
from typing import Any, Tuple, Type, Union
import werkzeug.exceptions

BaseHandler: Any
Config: Any
Database: Any
Forbidden: Type[werkzeug.exceptions.Forbidden]
InternalServerError: Type[werkzeug.exceptions.InternalServerError]
Logger: Any
NotFound: Type[werkzeug.exceptions.NotFound]
SECRET_LEN: Any
StorageManager: Any
decode: Any
decode_data: Any
gevent: Any
nacl: module
os: module
platform: module
recover_file_password: Any
shutil: module
suppress: Type[contextlib.suppress]
time: module
traceback: module
yaml: module
zipfile: module

class ContestManager:
    has_contest: bool
    input_queue: dict
    tasks: dict
    @staticmethod
    def evaluate_output(task_name, input_path, output_path) -> Any: ...
    @staticmethod
    def extract_contest(token) -> None: ...
    @staticmethod
    def get_input(task_name, attempt) -> Tuple[Any, Any]: ...
    @staticmethod
    def import_contest(path) -> Any: ...
    @staticmethod
    def read_from_disk(remove_enc = ...) -> None: ...
    @staticmethod
    def system_extension() -> str: ...
    @staticmethod
    def worker(task_name) -> Any: ...

def sha256(__string: Union[bytearray, bytes, memoryview] = ...) -> hashlib._Hash: ...
