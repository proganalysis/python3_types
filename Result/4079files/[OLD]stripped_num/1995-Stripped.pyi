# (generated with --quick)

from typing import Any, List, Tuple, Type

IgniteDataType: Any
__all__: List[str]
ctypes: module

class BoolObject(DataObject):
    c_type: Type[ctypes.c_bool]
    default: bool
    pythonic: Type[bool]
    type_code: Any

class ByteObject(DataObject):
    c_type: Type[ctypes.c_byte]
    default: int
    pythonic: Type[int]
    type_code: Any

class CharObject(DataObject):
    __doc__: str
    c_type: Type[ctypes.c_short]
    default: str
    pythonic: Type[str]
    type_code: Any
    @classmethod
    def from_python(cls, value) -> Any: ...
    @classmethod
    def to_python(cls, ctype_object, *args, **kwargs) -> Any: ...

class DataObject(Any):
    __doc__: str
    _object_c_type: None
    c_type: None
    type_code: None
    @classmethod
    def build_c_type(cls) -> Any: ...
    @classmethod
    def from_python(cls, value) -> bytes: ...
    @classmethod
    def parse(cls, client) -> Tuple[Any, Any]: ...
    @staticmethod
    def to_python(ctype_object, *args, **kwargs) -> Any: ...

class DoubleObject(DataObject):
    c_type: Type[ctypes.c_double]
    default: float
    pythonic: Type[float]
    type_code: Any

class FloatObject(DataObject):
    c_type: Type[ctypes.c_float]
    default: float
    pythonic: Type[float]
    type_code: Any

class IntObject(DataObject):
    c_type: Type[ctypes.c_int]
    default: int
    pythonic: Type[int]
    type_code: Any

class LongObject(DataObject):
    c_type: Type[ctypes.c_longlong]
    default: int
    pythonic: Type[int]
    type_code: Any

class ShortObject(DataObject):
    c_type: Type[ctypes.c_short]
    default: int
    pythonic: Type[int]
    type_code: Any

def __getattr__(name) -> Any: ...
