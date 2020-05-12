# (generated with --quick)

import abc
from typing import Any, Callable, Dict, List, Tuple, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
fileinput: module
logger: logging.Logger
logging: module
lxd: Any
pickle: module
shutil: module
util: Any

_FuncT = TypeVar('_FuncT', bound=Callable)

class AbstractRunner(metaclass=abc.ABCMeta):
    @abstractmethod
    def run(self, container_name, filename, function_name, input_str) -> Any: ...

class CodeRunner(AbstractRunner):
    run_script_filename: str
    util_files: List[str]
    def __init__(self, language) -> None: ...
    def run(self, container_name, code_filename, function_name, input_tuples) -> Tuple[list, List[Dict[str, Any]]]: ...

class EngineExecutionError(Exception):
    def __init__(self, message) -> None: ...

class FilePullError(Exception):
    def __init__(self, message) -> None: ...

class FilePushError(Exception):
    def __init__(self, message) -> None: ...

def abstractmethod(callable: _FuncT) -> _FuncT: ...
