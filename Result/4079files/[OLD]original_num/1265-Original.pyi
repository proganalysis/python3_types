# (generated with --quick)

import __future__
import io
from typing import Any, BinaryIO, IO, Iterator, Optional, Type, TypeVar, Union

BytesIO: Type[io.BytesIO]
absolute_import: __future__._Feature
also_image: bytes
args: list
binascii: module
division: __future__._Feature
im: BinaryIO
image: Any
in_image: FirmwareImage
options: optparse.Values
optparse: module
os: module
out_file: str
out_image: FirmwareImage
parser: optparse.OptionParser
patchee: Any
print_function: __future__._Feature
struct: module
sys: module
unicode_literals: __future__._Feature

_TFirmwareImage = TypeVar('_TFirmwareImage', bound=FirmwareImage)

class AppDescriptor(object):
    LENGTH: int
    RESERVED: bytes
    SIGNATURE: bytes
    __doc__: str
    empty: Any
    image_crc: Any
    image_size: Any
    reserved: Any
    signature: Any
    valid: Any
    vcs_commit: Any
    version_major: Any
    version_minor: Any
    def __init__(self, bytes = ...) -> None: ...
    def pack(self) -> bytes: ...
    def unpack(self, bytes) -> None: ...

class FirmwareImage(object):
    PADDING: int
    _contents: io.BytesIO
    _descriptor: Optional[AppDescriptor]
    _descriptor_bytes: Optional[bytes]
    _descriptor_offset: Optional[int]
    _do_write: bool
    _file: IO[Union[bytes, str]]
    _length: Optional[int]
    _padding: int
    app_descriptor: Any
    app_descriptor_offset: Any
    crc: int
    length: Any
    def __enter__(self: _TFirmwareImage) -> _TFirmwareImage: ...
    def __exit__(self, *args) -> None: ...
    def __getattr__(self, attr) -> Any: ...
    def __init__(self, path, mode = ...) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def _write_descriptor_raw(self) -> None: ...
    def write_descriptor(self) -> None: ...
