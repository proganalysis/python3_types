# (generated with --quick)

from typing import Any, List, Optional

socket: module
struct: module

class LibPeProtocol:
    CMD_RECEIVE_ERROR: int
    CMD_RECEIVE_SUCCESS: int
    CMD_SEND_ECHO: int
    CMD_SEND_GET_CONFIG: int
    CMD_SEND_PARAM_BOOL: List[int]
    CMD_SEND_PARAM_BYTE: List[int]
    CMD_SEND_PARAM_INT: List[int]
    CMD_SEND_PARAM_STR: List[int]
    CMD_SEND_PARAM_VOID: List[int]
    CMD_SEND_RESTART: int
    CMD_SEND_SET_CONTROL_INTERFACE: int
    CMD_SEND_SET_CONTROL_PORT: int
    CMD_SEND_SET_DATA_INTERFACE: int
    CMD_SEND_SET_DATA_PORT: int
    CMD_SEND_SET_ENABLE: int
    CMD_SEND_SET_ENCRYPT: int
    CMD_SEND_SET_ENCRYPT_ITERATIONS: int
    CMD_SEND_SET_METHOD_ALIGNMENT: int
    CMD_SEND_SET_METHOD_ALIGNMENT_RESIZE: int
    CMD_SEND_SET_METHOD_CHANGE_FLAGS: int
    CMD_SEND_SET_METHOD_CROSS_SECTION_JUMP: int
    CMD_SEND_SET_METHOD_CROSS_SECTION_JUMP_ITERATIONS: int
    CMD_SEND_SET_METHOD_NEW_SECTION: int
    CMD_SEND_SET_PAYLOAD_NAME_X64: int
    CMD_SEND_SET_PAYLOAD_NAME_X86: int
    CMD_SEND_SET_PAYLOAD_X64: int
    CMD_SEND_SET_PAYLOAD_X86: int
    CMD_SEND_SET_RANDOM_SECTION_NAME: int
    CMD_SEND_SET_REMOVE_INTEGRITY_CHECK: int
    CMD_SEND_SET_SECTION_NAME: int
    CMD_SEND_SET_TOKEN: int
    CMD_SEND_SET_TRY_STAY_STEALTH: int
    CMD_SEND_SHUTDOWN: int
    host: Any
    last_error: Optional[str]
    max_size: Any
    port: Any
    timeout: Any
    token: bytes
    def __init__(self, token, host, port, timeout = ..., max_size = ...) -> None: ...
    def get_last_error(self) -> Any: ...
    def send_command(self, command, data) -> Optional[bytes]: ...
    def set_token(self, token) -> bool: ...
