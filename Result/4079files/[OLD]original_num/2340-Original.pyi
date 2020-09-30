# (generated with --quick)

import pathlib
from typing import Any, Generator, Type

File: Any
Path: Type[pathlib.Path]
datetime: Type[datetime.datetime]
logging: module
models: Any
os: module
re: module
settings: Any
zipfile: module

class ResumableFile(object):
    base_filename: Any
    chunk_exists: Any
    chunk_names: list
    chunk_suffix: str
    current_chunk_name: str
    file: Any
    filename: Any
    image_allow: Any
    is_complete: bool
    kwargs: Any
    size: Any
    storage: Any
    video_allow: Any
    def __init__(self, storage, kwargs) -> None: ...
    def chunks(self) -> Generator[Any, Any, None]: ...
    def delete_chunks(self) -> None: ...
    def process_chunk(self, file) -> None: ...
    def resotre_file(self) -> None: ...
    def save_model(self, model, save_path, request) -> None: ...
