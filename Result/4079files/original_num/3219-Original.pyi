# (generated with --quick)

from typing import Any, Union

Logger: Any
SimpleJSONRPCRequestHandler: Any
SimpleJSONRPCServer: Any
time: module
util: Any

class RPCAuthCredentialsInvalid(Exception): ...

class RPCAuthCredentialsMissing(Exception): ...

class RPCAuthUnsupportedType(Exception): ...

class VerifyingJSONRPCServer(Any, Any):
    rpc_password: Any
    rpc_user: Any
    def __init__(self, *args, rpc_user, rpc_password, **kargs) -> None: ...
    def authenticate(self, headers) -> None: ...

def b64decode(s: Union[bytes, str], altchars: bytes = ..., validate: bool = ...) -> bytes: ...
