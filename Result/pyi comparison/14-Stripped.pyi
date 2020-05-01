# (generated with --quick)

from typing import Any, Generator, Sequence, Tuple, TypeVar

AppInstance: Any
BagMessage: Any
BagReader: Any
BagWriter: Any
Input: Any
InputInjector: Any
Message: Any
Mutation: Any
Mutator: Any
TypeDatabase: Any
__all__: Tuple[str, str]
attr: module
bisect: module
logger: logging.Logger
logging: module
os: module
random: module
tempfile: module
threading: module
time: module

_TBag = TypeVar('_TBag', bound=Bag)

class Bag(Sequence):
    __doc__: str
    _contents: Any
    def __getitem__(self, index) -> Any: ...
    def __init__(self, contents) -> None: ...
    def __iter__(self) -> Generator[nothing, Any, None]: ...
    def __len__(self) -> int: ...
    def delete(self: _TBag, index) -> _TBag: ...
    def insert(self: _TBag, message) -> _TBag: ...
    @classmethod
    def load(cls, db_type, fn, topics = ...) -> Bag: ...
    def replace(self: _TBag, index, replacement) -> _TBag: ...
    def restrict_to_topic(self: _TBag, topic) -> _TBag: ...
    def save(self, fn) -> None: ...
    def swap(self: _TBag, i, j) -> _TBag: ...

class BagInjector(Any):
    __doc__: str
    def __call__(self, app_instance, has_failed, inp) -> None: ...

class BagMutation(Any):
    __doc__: str

class DelayMessage(BagMutation):
    __doc__: str
    index: Any
    secs: Any
    def __call__(self, bag) -> Any: ...
    def __init__(self, index, secs) -> None: ...

class DropMessage(BagMutation):
    __doc__: str
    index: Any
    def __call__(self, bag) -> Any: ...
    def __init__(self, index) -> None: ...

class DropMessageMutator(Any):
    __doc__: str
    def __call__(self, inp) -> Any: ...

class InsertMessage(BagMutation):
    __doc__: str
    message: Any
    def __call__(self, bag) -> Any: ...
    def __init__(self, message) -> None: ...

class ReplaceMessage(BagMutation):
    __doc__: str
    index: Any
    replacement: Any
    def __call__(self, bag) -> Any: ...
    def __init__(self, index, replacement) -> None: ...

class ReplaceMessageData(BagMutation):
    __doc__: str
    index: Any
    replacement: Any
    def __call__(self, bag) -> Any: ...
    def __init__(self, index, replacement) -> None: ...

class SwapMessage(BagMutation):
    __doc__: str
    index_a: Any
    index_b: Any
    def __call__(self, bag) -> Any: ...
    def __init__(self, index_a, index_b) -> None: ...
