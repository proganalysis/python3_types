import asyncio
from framework import Example
from typing import Any

def file_sender(writer: Any, file_: Any, size: Any, show_progress: Any) -> None: ...

class Upload(Example):
    VALID_MIME_RE: Any = ...
    DEFAULT_MIME_TYPE: str = ...
    def prepare_argparse(self): ...
    service_addr: Any = ...
    file: Any = ...
    file_name: Any = ...
    file_size: Any = ...
    file_type: Any = ...
    show_progress: Any = ...
    def configure(self) -> None: ...
    @asyncio.coroutine
    def _check_for_upload_service(self, disco: Any, jid: Any): ...
    async def upload(self, url: Any, headers: Any): ...
    @asyncio.coroutine
    def run_simple_example(self) -> None: ...
