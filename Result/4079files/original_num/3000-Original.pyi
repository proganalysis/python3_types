# (generated with --quick)

import __builtin__
from typing import Any, Dict, List

Git: None
Hg: None
abc: module
datetime: module
enum: module
functools: module
git: Any
hashlib: module
hglib: Any
pathlib: module
sys: module
types: module

class Repo(metaclass=abc.ABCMeta):
    __doc__: str
    branch: Any
    claimed_commits: List[types.SimpleNamespace]
    commits: Any
    directory: pathlib.Path
    remote: str
    supported: Dict[Any, __builtin__.type]
    type: None
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def __init__(self, remote: str, parent_path: pathlib.Path, *, branch = ...) -> None: ...
    def claim_commit(self, name, id_) -> None: ...
    @abstractmethod
    def clone(self) -> Any: ...
    @abstractmethod
    def close(self) -> Any: ...
    @classmethod
    def get(cls, type_: str, remote: str, dest_parent: str, *, branch = ...) -> Any: ...
    @abstractmethod
    def log(self, name) -> Any: ...
    @classmethod
    def register(cls, subclass) -> None: ...
    @abstractmethod
    def update(self) -> Any: ...

class Supported(enum.Enum):
    git: int
    hg: int

def create_log_entry(id_, date, author) -> types.SimpleNamespace: ...
