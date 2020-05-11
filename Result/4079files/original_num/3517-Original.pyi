# (generated with --quick)

import pyrcrack.executor
from typing import Any, Coroutine, Type

ExecutorHelper: Type[pyrcrack.executor.ExecutorHelper]
asyncio: module
parse: Any

class AireplayNg(pyrcrack.executor.ExecutorHelper):
    __doc__: str
    command: str
    requires_tempdir: bool
    requires_tempfile: bool
    def get_results(self) -> Coroutine[Any, Any, list]: ...
    def result_updater(self) -> Coroutine[Any, Any, None]: ...
