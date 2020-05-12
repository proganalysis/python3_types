import asyncio
from ..psychrometrics import DOMAIN as DOMAIN, PsychrometricsSensor as PsychrometricsSensor
from typing import Any, Optional

DEPENDENCIES: Any

@asyncio.coroutine
def async_setup_platform(hass: Any, config: Any, async_add_devices: Any, discovery_info: Optional[Any] = ...) -> None: ...
