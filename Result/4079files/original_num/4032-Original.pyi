# (generated with --quick)

from typing import Any, NoReturn

CASCManager: Any
DLLRecord: Any
File: Any
FileAccess: Any
FileMode: Any
ImageDefinition: Any
MemoryStream: Any
OWTexture: Any
Record: Any
STUD: Any
Stream: Any
load_dll: Any
os: module

class OWDecal(Any):
    @classmethod
    def _from_stream(cls, stream, man) -> Any: ...
    @classmethod
    def from_casc(cls, file: str, man) -> Any: ...
    @classmethod
    def from_file(cls, file: str, man) -> Any: ...
    @classmethod
    def from_record(cls, record, man) -> Any: ...
    @classmethod
    def from_record_with_data(cls, record, record_data, man) -> NoReturn: ...
    @staticmethod
    def get_04D_name(file_name: str, stream = ..., close_stream: bool = ...) -> NoReturn: ...
    @staticmethod
    def requires_04D(file_004: str, close: bool = ...) -> NoReturn: ...
