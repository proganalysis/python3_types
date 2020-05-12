import typing
from .aio_method_ctx import AioMethodContext
from aiohttp import web
from spyne import Application
from spyne.model.fault import Fault
from spyne.server import ServerBase
from typing import Any

logger: Any

class AioBase(ServerBase):
    transport: str = ...
    _chunked: Any = ...
    _mtx_build_interface_document: Any = ...
    _wsdl: Any = ...
    _thread_pool: Any = ...
    def __init__(self, app: Application, chunked: bool=..., threads: typing.Optional[int]=...) -> None: ...
    @staticmethod
    async def make_streaming_response(req: web.Request, status: int, content: typing.List[bytes], chunked: bool=..., headers: typing.Optional[dict]=...) -> Any: ...
    async def response(self, req: web.Request, p_ctx: AioMethodContext, others: list, error: typing.Optional[Fault]=...) -> web.StreamResponse: ...
    async def handle_error(self, req: web.Request, p_ctx: AioMethodContext, others: list, error: typing.Optional[Fault]) -> web.StreamResponse: ...
    async def handle_wsdl_request(self, req: web.Request, app: web.Application) -> web.StreamResponse: ...
    async def handle_rpc_request(self, req: web.Request, app: web.Application) -> web.StreamResponse: ...
    def _handle_rpc_body(self, p_ctx: Any) -> typing.Optional[Fault]: ...
