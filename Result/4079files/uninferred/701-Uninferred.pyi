from typing import Any

def setup_txaio(event_loop: Any) -> None: ...
async def context() -> None: ...
async def wampclient(request: Any, context: Any) -> None: ...