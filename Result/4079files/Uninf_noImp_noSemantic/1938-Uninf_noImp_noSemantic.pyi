from thrift.Thrift import *
from typing import Any, Optional

class TProtocolException(TException):
    UNKNOWN: int = ...
    INVALID_DATA: int = ...
    NEGATIVE_SIZE: int = ...
    SIZE_LIMIT: int = ...
    BAD_VERSION: int = ...
    INVALID_PROTOCOL: int = ...
    MISSING_REQUIRED_FIELD: int = ...
    type: Any = ...
    def __init__(self, type: Any = ..., message: Optional[Any] = ...) -> None: ...

class TProtocolBase:
    trans: Any = ...
    def __init__(self, trans: Any) -> None: ...
    def writeMessageBegin(self, name: Any, ttype: Any, seqid: Any) -> None: ...
    def writeMessageEnd(self) -> None: ...
    def writeStructBegin(self, name: Any) -> None: ...
    def writeStructEnd(self) -> None: ...
    def writeUnionBegin(self, name: Any) -> None: ...
    def writeUnionEnd(self) -> None: ...
    def writeFieldBegin(self, name: Any, type: Any, id: Any) -> None: ...
    def writeFieldEnd(self) -> None: ...
    def writeFieldStop(self) -> None: ...
    def writeMapBegin(self, ktype: Any, vtype: Any, size: Any) -> None: ...
    def writeMapEnd(self) -> None: ...
    def writeListBegin(self, etype: Any, size: Any) -> None: ...
    def writeListEnd(self) -> None: ...
    def writeSetBegin(self, etype: Any, size: Any) -> None: ...
    def writeSetEnd(self) -> None: ...
    def writeBool(self, bool_val: Any) -> None: ...
    def writeByte(self, byte: Any) -> None: ...
    def writeI16(self, i16: Any) -> None: ...
    def writeI32(self, i32: Any) -> None: ...
    def writeI64(self, i64: Any) -> None: ...
    def writeDouble(self, dub: Any) -> None: ...
    def writeFloat(self, flt: Any) -> None: ...
    def writeString(self, str: Any) -> None: ...
    def readMessageBegin(self) -> None: ...
    def readMessageEnd(self) -> None: ...
    def readStructBegin(self) -> None: ...
    def readStructEnd(self) -> None: ...
    def readFieldBegin(self) -> None: ...
    def readFieldEnd(self) -> None: ...
    def readMapBegin(self) -> None: ...
    def readMapEnd(self) -> None: ...
    def readListBegin(self) -> None: ...
    def readListEnd(self) -> None: ...
    def readSetBegin(self) -> None: ...
    def readSetEnd(self) -> None: ...
    def readBool(self) -> None: ...
    def readByte(self) -> None: ...
    def readI16(self) -> None: ...
    def readI32(self) -> None: ...
    def readI64(self) -> None: ...
    def readDouble(self) -> None: ...
    def readFloat(self) -> None: ...
    def readString(self) -> None: ...
    def skip(self, type: Any) -> None: ...
    def readIntegral(self, type: Any): ...
    def readFloatingPoint(self, type: Any): ...

class TProtocolFactory:
    def getProtocol(self, trans: Any) -> None: ...
