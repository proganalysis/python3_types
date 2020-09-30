# (generated with --quick)

from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar

LinkInfo = `namedtuple-LinkInfo-link-name-sections`

Validator: Any
collections: module
re: module
typing: module

_Tnamedtuple-LinkInfo-link-name-sections = TypeVar('_Tnamedtuple-LinkInfo-link-name-sections', bound=`namedtuple-LinkInfo-link-name-sections`)

class Document:
    content: list
    description: Any
    title: Any
    url: Any
    version: Any
    def __init__(self, content = ..., url = ..., title = ..., description = ..., version = ...) -> None: ...
    def get_links(self) -> list: ...
    def get_sections(self) -> list: ...
    def walk_links(self) -> list: ...

class Field:
    description: Any
    example: Any
    location: Any
    name: Any
    required: Any
    schema: Any
    title: Any
    def __init__(self, name, location, title = ..., description = ..., required = ..., schema = ..., example = ...) -> None: ...

class Link:
    __doc__: str
    description: Any
    encoding: Any
    fields: list
    handler: Any
    method: Any
    name: Any
    response: Any
    title: Any
    url: Any
    def __init__(self, url, method, handler = ..., name = ..., encoding = ..., response = ..., title = ..., description = ..., fields = ...) -> None: ...
    def get_body_field(self) -> Any: ...
    def get_expanded_body(self) -> Any: ...
    def get_path_fields(self) -> list: ...
    def get_query_fields(self) -> list: ...

class Response:
    encoding: Any
    schema: Any
    status_code: Any
    def __init__(self, encoding, status_code = ..., schema = ...) -> None: ...

class Section:
    content: list
    description: Any
    name: Any
    title: Any
    def __init__(self, name, content = ..., title = ..., description = ...) -> None: ...
    def get_links(self) -> list: ...
    def get_sections(self) -> list: ...
    def walk_links(self, previous_sections = ...) -> list: ...

class `namedtuple-LinkInfo-link-name-sections`(tuple):
    __slots__ = ["link", "name", "sections"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str]
    link: Any
    name: Any
    sections: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-LinkInfo-link-name-sections`], link, name, sections) -> `_Tnamedtuple-LinkInfo-link-name-sections`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-LinkInfo-link-name-sections`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-LinkInfo-link-name-sections`: ...
    def _replace(self: `_Tnamedtuple-LinkInfo-link-name-sections`, **kwds) -> `_Tnamedtuple-LinkInfo-link-name-sections`: ...
