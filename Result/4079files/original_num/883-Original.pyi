# (generated with --quick)

import array
import io
import mmap
from typing import Any, Type, Union

BitArrayStream: Any
Cable: Any
CableColor: Any
CableType: Any
FileIO: Type[io.FileIO]
Location: Any
Module: Any
ModuleParameters: Any
Patch: Any
ProjectData: Any
bitarray: Any
transform_in2in_cables: Any

def parse_cable_list(blob, patch) -> None: ...
def parse_data_object(head: int, blob, patch, ctx: dict) -> None: ...
def parse_header(pch2: io.FileIO, patch) -> None: ...
def parse_location(loc: int) -> Any: ...
def parse_module_list(blob, patch) -> None: ...
def parse_module_parameters(blob, patch) -> None: ...
def parse_pch2(data, pch2_file: str, convert_in2in = ...) -> Any: ...
def unpack(fmt: Union[bytes, str], buffer: Union[bytearray, bytes, memoryview, mmap.mmap, array.array[int]]) -> tuple: ...
