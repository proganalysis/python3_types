# (generated with --quick)

from typing import Any

AUTOMATION_ARGS: Any
Browser: Any
DEFAULT_ARGS: Any
Launcher: Any
asyncio: module
check_chromium: Any
chromium_executable: Any
download_chromium: Any
get_free_port: Any
logging: module
merge_dict: Any

class HeadLessLauncher(Any):
    __doc__: str
    _loop: Any
    _tmp_user_data_dir: None
    chromeClosed: bool
    chrome_args: list
    cmd: list
    `exec`: Any
    options: Any
    port: Any
    url: str
    def __init__(self, options = ..., **kwargs) -> None: ...

def launch(options = ..., **kwargs) -> coroutine: ...
