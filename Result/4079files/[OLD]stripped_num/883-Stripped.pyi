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
def parse_data_object(head, blob, patch, ctx) -> None: ...
def parse_header(pch2, patch) -> None: ...
def parse_location(loc) -> Any: ...
def parse_module_list(blob, patch) -> None: ...
def parse_module_parameters(blob, patch) -> None: ...
def parse_pch2(data, pch2_file, convert_in2in = ...) -> Any: ...
def unpack(fmt: Union[bytes, str], buffer: Union[bytearray, bytes, memoryview, mmap.mmap, array.array[int]]) -> tuple: ...
