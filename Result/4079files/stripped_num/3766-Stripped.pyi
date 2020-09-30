# (generated with --quick)

import codecs
import json
import json.decoder
import json.encoder
from typing import Any, Callable, Dict, IO, Iterator, List, Optional, Pattern, Tuple, Type, TypeVar, Union

basepath: Any
checker: Pattern[str]
command: Dict[str, Any]
configparser: module
content: list
dest: str
dirs: List[str]
emote: Any
emotepath: str
emotes: Dict[nothing, nothing]
f: codecs.StreamReaderWriter
filename: str
files: List[str]
glitchFixed: List[nothing]
is_unprintable: Pattern[str]
jsondata: Any
jsonpath: Any
jsonpathend: Any
jsonpaths: Any
label: Any
labelsTotal: Dict[nothing, nothing]
labelsTotalN: Any
labelsTranslated: Dict[nothing, nothing]
labelsTranslatedN: Any
mod_dir: str
originfile: Any
others_dest: str
others_path: str
patchfile: str
patchfiles: Dict[str, list]
pfile: str
restpath: str
sep: str
specialpaths: List[str]
specials: Dict[str, dict]
subdir: str
text: Any
textpath: str
thecontent: list
thefile: str
translation: Any
translations_dir: str

AnyStr = TypeVar('AnyStr', str, bytes)

def add_count(counter, path, value) -> None: ...
def basename(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def check_translation_length(text) -> bool: ...
def copen(filename: str, mode: str = ..., encoding: str = ..., errors: str = ..., buffering: int = ...) -> codecs.StreamReaderWriter: ...
def copy(src: Union[str, _PathLike[str]], dst: Union[str, _PathLike[str]], *, follow_symlinks: bool = ...) -> Any: ...
def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def dump(obj, fp: IO[str], skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., cls: Optional[Type[json.encoder.JSONEncoder]] = ..., indent: Optional[Union[int, str]] = ..., separators: Optional[Tuple[str, str]] = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ..., **kwds) -> None: ...
def exists(path: Union[_PathLike, bytes, int, str]) -> bool: ...
def field_by_path(obj, path, newval = ..., sep = ...) -> Any: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def load(fp: json._Reader, cls: Optional[Type[json.decoder.JSONDecoder]] = ..., object_hook: Optional[Callable[[dict], Any]] = ..., parse_float: Optional[Callable[[str], Any]] = ..., parse_int: Optional[Callable[[str], Any]] = ..., parse_constant: Optional[Callable[[str], Any]] = ..., object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]] = ..., **kwds) -> Any: ...
def makedirs(name: Union[_PathLike, bytes, str], mode: int = ..., exist_ok: bool = ...) -> None: ...
def normpath(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def regex(pattern: Union[Pattern[AnyStr], AnyStr], flags: int = ...) -> Pattern[AnyStr]: ...
@overload
def relpath(path: Union[bytes, _PathLike[bytes]], start: Optional[Union[bytes, _PathLike[bytes]]] = ...) -> bytes: ...
@overload
def relpath(path: Union[str, _PathLike[str]], start: Optional[Union[str, _PathLike[str]]] = ...) -> str: ...
def set_count(counter, path, value) -> None: ...
def sum_up_counter(counter) -> Any: ...
def uopen(path, mode) -> codecs.StreamReaderWriter: ...
def walk(top: Union[_PathLike[AnyStr], AnyStr], topdown: bool = ..., onerror: Optional[Callable[[OSError], Any]] = ..., followlinks: bool = ...) -> Iterator[Tuple[AnyStr, List[AnyStr], List[AnyStr]]]: ...
