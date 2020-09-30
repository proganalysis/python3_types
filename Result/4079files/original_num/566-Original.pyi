# (generated with --quick)

from typing import Any, Callable, Dict, List, NoReturn, Optional, Union

Command: Any
about: Dict[nothing, nothing]
codecs: module
f: codecs.StreamReaderWriter
find_packages: Any
here: str
long_description: str
os: module
required: List[nothing]
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
    def status(s) -> None: ...

def rmtree(path: Union[bytes, str, _PathLike[str]], ignore_errors: bool = ..., onerror: Optional[Callable[[Any, Any, Any], Any]] = ...) -> None: ...
