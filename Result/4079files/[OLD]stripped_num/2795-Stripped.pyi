# (generated with --quick)

from typing import Any, Callable, Dict, List, NoReturn, Optional, TextIO, Union

ABOUT: Dict[nothing, nothing]
AUTHOR: str
Command: Any
DESCRIPTION: str
EMAIL: str
HERE: str
LONG_DESC: str
NAME: str
REQUIRED: List[str]
REQUIRES_PYTHON: str
URL: str
VERSION: None
f: TextIO
find_packages: Any
io: module
os: module
setup: Any
sys: module

class UploadCommand(Any):
    __doc__: str
    description: str
    user_options: List[nothing]
    def finalize_options(self) -> None: ...
    def initialize_options(self) -> None: ...
    def run(self) -> NoReturn: ...
    @staticmethod
    def status(string) -> None: ...

def rmtree(path: Union[bytes, str, _PathLike[str]], ignore_errors: bool = ..., onerror: Optional[Callable[[Any, Any, Any], Any]] = ...) -> None: ...
