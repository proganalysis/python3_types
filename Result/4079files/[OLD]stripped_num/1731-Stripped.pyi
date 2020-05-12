# (generated with --quick)

import collections
from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar, Union

Finals = `namedtuple-Finals-pinyin-rhyme-tones`

jieba: Any
logging: module
pinyin: Any
pypinyin: Any

_Tnamedtuple-Finals-pinyin-rhyme-tones = TypeVar('_Tnamedtuple-Finals-pinyin-rhyme-tones', bound=`namedtuple-Finals-pinyin-rhyme-tones`)

class `namedtuple-Finals-pinyin-rhyme-tones`(tuple):
    __slots__ = ["pinyin", "rhyme", "tones"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str]
    pinyin: Any
    rhyme: Any
    tones: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Finals-pinyin-rhyme-tones`], pinyin, rhyme, tones) -> `_Tnamedtuple-Finals-pinyin-rhyme-tones`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Finals-pinyin-rhyme-tones`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Finals-pinyin-rhyme-tones`: ...
    def _replace(self: `_Tnamedtuple-Finals-pinyin-rhyme-tones`, **kwds) -> `_Tnamedtuple-Finals-pinyin-rhyme-tones`: ...

def finals_info(word) -> `namedtuple-Finals-pinyin-rhyme-tones`: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
