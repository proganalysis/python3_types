# (generated with --quick)

import contextlib
import pyrcrack.executor
import pyrcrack.models
from typing import Any, Coroutine, Dict, List, Type, TypeVar, Union

AccessPoint: Type[pyrcrack.models.AccessPoint]
Client: Type[pyrcrack.models.Client]
ExecutorHelper: Type[pyrcrack.executor.ExecutorHelper]
asyncio: module
csv: module
io: module
suppress: Type[contextlib.suppress]

AnyStr = TypeVar('AnyStr', str, bytes)

class AirodumpNg(pyrcrack.executor.ExecutorHelper):
    __doc__: str
    command: str
    csv_file: Any
    requires_tempdir: bool
    requires_tempfile: bool
    def get_results(self) -> Dict[str, List[Union[pyrcrack.models.AccessPoint, pyrcrack.models.Client]]]: ...
    def result_updater(self) -> Coroutine[Any, Any, None]: ...
    def sorted_aps(self) -> List[pyrcrack.models.AccessPoint]: ...

def glob(pathname: AnyStr, *, recursive: bool = ...) -> List[AnyStr]: ...
