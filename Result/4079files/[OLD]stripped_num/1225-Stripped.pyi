# (generated with --quick)

import asyncio.queues
from typing import Any, Coroutine, Type

CProtocol: Any
Queue: Type[asyncio.queues.Queue]
Response: Any
asyncio: module
static_response: bytes

def handle_dump(request, transport, response) -> None: ...
def handle_request(request, transport) -> Coroutine[Any, Any, None]: ...
def handle_request_block(request, transport, response) -> None: ...
def handle_requests(queue, transport) -> coroutine: ...
def make_class(flavor) -> Any: ...