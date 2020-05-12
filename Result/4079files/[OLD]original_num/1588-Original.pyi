# (generated with --quick)

import concurrent.futures.thread
from typing import Any, List, Tuple, Type

Config: Any
Controller: Any
InteractiveShellEmbed: Any
KytosConfig: Any
Prompts: Any
ThreadPoolExecutor: Type[concurrent.futures.thread.ThreadPoolExecutor]
Token: Any
__version__: Any
asyncio: module
daemon: Any
functools: module
signal: module

class KytosPrompt(Any):
    __doc__: str
    def in_prompt_tokens(self) -> List[Tuple[Any, str]]: ...

def async_main(config) -> None: ...
def main() -> None: ...
def start_shell(controller = ...) -> None: ...
