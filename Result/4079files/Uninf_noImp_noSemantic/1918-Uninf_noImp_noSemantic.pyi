from typing import Any

DB_HOST: str
DB_USERNAME: str
DB_PASSWORD: str
DB_NAME: str

def notification_manager(): ...
async def test_active_monitor_manager(notification_manager: Any) -> None: ...
async def test_create_active_monitor_def(notification_manager: Any) -> None: ...
