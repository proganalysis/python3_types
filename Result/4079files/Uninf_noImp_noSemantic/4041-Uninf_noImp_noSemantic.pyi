from typing import Any, List
from xcat.attack import AttackContext, Injection

injectors: Any

async def detect_injections(context: AttackContext) -> List[Injection]: ...
