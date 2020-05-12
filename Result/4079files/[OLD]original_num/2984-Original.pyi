# (generated with --quick)

from typing import Any, Callable, Dict, List, NoReturn, Optional, TextIO, Union

AUTHOR: str
Command: Any
DESCRIPTION: str
EMAIL: str
EXTRAS: Dict[nothing, nothing]
NAME: str
REQUIRED: list
REQUIRES_PYTHON: str
URL: str
VERSION: None
about: Dict[nothing, nothing]
f: TextIO
find_packages: Any
here: str
io: module
long_description: str
os: module
setup: Any
subprocess: module
sys: module

class UploadCommand(Any):
    __doc__: str
    description: str
    user_options: List[nothing]
    def finalize_options(self) -> None: ...
    def initialize_options(self) -> None: ...
    def run(self) -> NoReturn: ...
    @staticmethod
    def status(s) -> None: ...
    def twine_command(self) -> List[str]: ...

class UploadTestCommand(UploadCommand): ...

def rmtree(path: Union[bytes, str, _PathLike[str]], ignore_errors: bool = ..., onerror: Optional[Callable[[Any, Any, Any], Any]] = ...) -> None: ...
