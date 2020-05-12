# (generated with --quick)

import __builtin__
from typing import Any, Callable, List, Optional

tibrvEventCallback = Callable[[tibrvEvent, tibrvMsg, object], None]
tibrvEventOnComplete = Callable[[tibrvEvent, object], None]
tibrvEventVectorCallback = Callable[[List[tibrvMsg], int], None]
tibrvQueueHook = Callable[[tibrvQueue, object], None]
tibrvQueueOnComplete = Callable[[tibrvQueue, object], None]

TIBRVMSG_BOOL: int
TIBRVMSG_DATETIME: int
TIBRVMSG_DATETIME_STRING_SIZE: int
TIBRVMSG_ENCRYPTED: int
TIBRVMSG_F32: int
TIBRVMSG_F32ARRAY: int
TIBRVMSG_F64: int
TIBRVMSG_F64ARRAY: int
TIBRVMSG_FIELDNAME_MAX: int
TIBRVMSG_I16: int
TIBRVMSG_I16ARRAY: int
TIBRVMSG_I32: int
TIBRVMSG_I32ARRAY: int
TIBRVMSG_I64: int
TIBRVMSG_I64ARRAY: int
TIBRVMSG_I8: int
TIBRVMSG_I8ARRAY: int
TIBRVMSG_IPADDR32: int
TIBRVMSG_IPPORT16: int
TIBRVMSG_MSG: int
TIBRVMSG_MSGARRAY: int
TIBRVMSG_NONE: int
TIBRVMSG_NO_TAG: int
TIBRVMSG_OPAQUE: int
TIBRVMSG_STRING: int
TIBRVMSG_STRINGARRAY: int
TIBRVMSG_U16: int
TIBRVMSG_U16ARRAY: int
TIBRVMSG_U32: int
TIBRVMSG_U32ARRAY: int
TIBRVMSG_U64: int
TIBRVMSG_U64ARRAY: int
TIBRVMSG_U8: int
TIBRVMSG_U8ARRAY: int
TIBRVMSG_USER_FIRST: int
TIBRVMSG_USER_LAST: int
TIBRVMSG_XML: int
TIBRVQUEUE_DISCARD_FIRST: tibrvQueueLimitPolicy
TIBRVQUEUE_DISCARD_LAST: tibrvQueueLimitPolicy
TIBRVQUEUE_DISCARD_NEW: tibrvQueueLimitPolicy
TIBRVQUEUE_DISCARD_NONE: tibrvQueueLimitPolicy
TIBRV_DEFAULT_QUEUE: tibrvQueue
TIBRV_FALSE: int
TIBRV_INVALID_ID: int
TIBRV_IO_EVENT: tibrvEventType
TIBRV_LISTEN_EVENT: tibrvEventType
TIBRV_NO_WAIT: float
TIBRV_PROCESS_TRANSPORT: int
TIBRV_SUBJECT_MAX: int
TIBRV_TIMER_EVENT: tibrvEventType
TIBRV_TRUE: int
TIBRV_WAIT_FOREVER: float
_ctypes: module
_time: module

class tibrvDispatchable(int):
    def __init__(self, val: int) -> None: ...

class tibrvDispatcher(int):
    def __init__(self, val: int) -> None: ...

class tibrvEvent(int):
    def __init__(self, val: int) -> None: ...

class tibrvEventType(int):
    def __init__(self, val: int) -> None: ...

class tibrvIOType(int):
    def __init__(self, val: int) -> None: ...

class tibrvId(int):
    def __init__(self, val: int) -> None: ...

class tibrvMsg(int):
    def __init__(self, val: int) -> None: ...

class tibrvMsgDateTime:
    _nsec: int
    _sec: int
    nsec: Any
    sec: Any
    def __eq__(self, other) -> bool: ...
    def __init__(self) -> None: ...
    def __str__(self) -> str: ...
    @staticmethod
    def now() -> tibrvMsgDateTime: ...

class tibrvMsgField:
    _count: int
    _data: None
    _id: int
    _name: Optional[__builtin__.str]
    _size: int
    _type: int
    count: int
    data: Any
    f32: Any
    f64: Any
    id: int
    int16: Any
    int32: Any
    int64: Any
    int8: Any
    msg: Any
    name: __builtin__.str
    size: int
    str: Any
    type: int
    uint16: Any
    uint32: Any
    uint64: Any
    uint8: Any
    def __init__(self, name: Optional[__builtin__.str] = ..., id: int = ...) -> None: ...

class tibrvQueue(int):
    def __init__(self, val: int) -> None: ...

class tibrvQueueGroup(int):
    def __init__(self, val: int) -> None: ...

class tibrvQueueLimitPolicy(int):
    def __init__(self, val: int) -> None: ...

class tibrvTransport(int):
    def __init__(self, val: int) -> None: ...

class tibrv_status(int):
    def __init__(self, val: int) -> None: ...
