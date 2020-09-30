from typing import Any

PREFIX_IP: str
PREFIX_USER: str

async def inc(op: str, id: str, period_secs: int, max_operations: int) -> Any: ...
async def create_indexes() -> None: ...
