# (generated with --quick)

import asyncio.locks
import concurrent.futures.thread
from typing import Any, Optional, Sequence, Tuple, Type, TypeVar, Union

AioMethodContext: Any
Application: Any
Fault: Any
HttpRpc: Any
ServerBase: Any
ThreadPoolExecutor: Type[concurrent.futures.thread.ThreadPoolExecutor]
asyncio: module
functools: module
get_fault_string_from_exception: Any
logger: logging.Logger
logging: module
process_contexts: Any
typing: module
web: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class AioBase(Any):
    _chunked: Any
    _mtx_build_interface_document: asyncio.locks.Lock
    _thread_pool: Optional[concurrent.futures.thread.ThreadPoolExecutor]
    _wsdl: Any
    transport: str
    def __init__(self, app, chunked = ..., threads = ...) -> None: ...
    def _handle_rpc_body(self, p_ctx) -> Any: ...
    def handle_error(self, req, p_ctx, others, error) -> coroutine: ...
    def handle_rpc_request(self, req, app) -> coroutine: ...
    def handle_wsdl_request(self, req, app) -> coroutine: ...
    @staticmethod
    def make_streaming_response(req, status, content, chunked = ..., headers = ...) -> coroutine: ...
    def response(self, req, p_ctx, others, error = ...) -> coroutine: ...

def urlunparse(components: Union[Sequence[Optional[AnyStr]], Tuple[Optional[AnyStr], Optional[AnyStr], Optional[AnyStr], Optional[AnyStr], Optional[AnyStr], Optional[AnyStr]]]) -> AnyStr: ...
