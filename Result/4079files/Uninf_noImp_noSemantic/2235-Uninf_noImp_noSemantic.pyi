from glob import glob as glob
from syncrypt.auth import CredentialsAuthenticationProvider
from syncrypt.backends import BinaryStorageBackend as BinaryStorageBackend, LocalStorageBackend as LocalStorageBackend
from syncrypt.backends.binary import get_manager_instance as get_manager_instance
from syncrypt.config import AppConfig
from syncrypt.models import store as store
from syncrypt.utils.logging import setup_logging as setup_logging
from typing import Any, Optional

class TestAuthenticationProvider(CredentialsAuthenticationProvider):
    def __init__(self) -> None: ...

class TestAppConfig(AppConfig):
    def __init__(self, config_file: Any, remote: Optional[Any] = ...) -> None: ...

def working_dir(): ...
async def local_app(working_dir: Any) -> None: ...
async def asyncio_loop() -> None: ...
async def local_daemon_app(working_dir: Any, asyncio_loop: Any) -> None: ...
async def local_api_client(local_daemon_app: Any, asyncio_loop: Any) -> None: ...
def assertSameFilesInFolder(self, *folders: Any): ...
async def test_vault(working_dir: Any): ...
async def empty_vault(working_dir: Any): ...
async def local_vault(local_app: Any, test_vault: Any) -> None: ...
async def local_daemon_vault(local_daemon_app: Any, working_dir: Any, test_vault: Any) -> None: ...
