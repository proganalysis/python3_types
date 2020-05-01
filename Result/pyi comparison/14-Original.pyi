# (generated with --quick)

from typing import Any, Iterator, List, Optional, Sequence, Tuple, TypeVar

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
    _contents: tuple
    def __getitem__(self, index) -> Any: ...
    def __init__(self, contents: tuple) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def delete(self: _TBag, index: int) -> _TBag: ...
    def insert(self: _TBag, message) -> _TBag: ...
    @classmethod
    def load(cls, db_type, fn: str, topics: Optional[List[str]] = ...) -> Bag: ...
    def replace(self: _TBag, index: int, replacement) -> _TBag: ...
    def restrict_to_topic(self: _TBag, topic: str) -> _TBag: ...
    def save(self, fn: str) -> None: ...
    def swap(self: _TBag, i: int, j: int) -> _TBag: ...

class BagInjector(Any):
    __doc__: str
    def __call__(self, app_instance, has_failed: threading.Event, inp) -> None: ...

class BagMutation(Any):
    __doc__: str

class DelayMessage(BagMutation):
    __doc__: str
    index: int
    secs: int
    def __call__(self, bag: Bag) -> Bag: ...
    def __init__(self, index: int, secs: int) -> None: ...

class DropMessage(BagMutation):
    __doc__: str
    index: int
    def __call__(self, bag: Bag) -> Bag: ...
    def __init__(self, index: int) -> None: ...

class DropMessageMutator(Any):
    __doc__: str
    def __call__(self, inp) -> Any: ...

class InsertMessage(BagMutation):
    __doc__: str
    message: Any
    def __call__(self, bag: Bag) -> Bag: ...
    def __init__(self, message) -> None: ...

class ReplaceMessage(BagMutation):
    __doc__: str
    index: int
    replacement: Any
    def __call__(self, bag: Bag) -> Bag: ...
    def __init__(self, index: int, replacement) -> None: ...

class ReplaceMessageData(BagMutation):
    __doc__: str
    index: int
    replacement: Any
    def __call__(self, bag: Bag) -> Bag: ...
    def __init__(self, index: int, replacement) -> None: ...

class SwapMessage(BagMutation):
    __doc__: str
    index_a: int
    index_b: int
    def __call__(self, bag: Bag) -> Bag: ...
    def __init__(self, index_a: int, index_b: int) -> None: ...
