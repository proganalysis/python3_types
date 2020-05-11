# (generated with --quick)

from typing import Any, List, TypeVar

APIClient: Any
AppConfig: Any
BinaryStorageBackend: Any
CredentialsAuthenticationProvider: Any
LocalStorageBackend: Any
SyncryptApp: Any
SyncryptDaemonApp: Any
Vault: Any
asyncio_loop: Any
empty_vault: Any
get_manager_instance: Any
local_api_client: Any
local_app: Any
local_daemon_app: Any
local_daemon_vault: Any
local_vault: Any
os: module
pytest: Any
setup_logging: Any
shutil: module
store: Any
test_vault: Any
trio: Any
trio_asyncio: Any
unittest: module
working_dir: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class TestAppConfig(Any):
    def __init__(self, config_file, remote = ...) -> None: ...

class TestAuthenticationProvider(Any):
    def __init__(self) -> None: ...

def assertSameFilesInFolder(self, *folders) -> None: ...
def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
