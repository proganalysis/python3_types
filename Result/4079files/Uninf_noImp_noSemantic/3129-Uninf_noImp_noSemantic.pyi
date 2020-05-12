import asyncio
from ..psychrometrics import DOMAIN as DOMAIN, PsychroCam as PsychroCam
from typing import Any

DEPENDENCIES: Any

@asyncio.coroutine
def async_setup_platform(hass: Any, config: Any, async_add_devices: Any, discovery_info: Any) -> None: ...
