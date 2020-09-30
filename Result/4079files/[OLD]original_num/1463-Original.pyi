# (generated with --quick)

from typing import Any, Callable, Iterable, List, Optional, Sequence, Sized, Tuple, Type, TypeVar, Union

LinkInfo = `namedtuple-LinkInfo-link-name-sections`

Validator: Any
collections: module
re: module
typing: module

_Tnamedtuple-LinkInfo-link-name-sections = TypeVar('_Tnamedtuple-LinkInfo-link-name-sections', bound=`namedtuple-LinkInfo-link-name-sections`)

class Document:
    content: List[Union[Link, Section]]
    description: str
    title: str
    url: str
    version: str
    def __init__(self, content: Optional[Sequence[Union[Link, Section]]] = ..., url: str = ..., title: str = ..., description: str = ..., version: str = ...) -> None: ...
    def get_links(self) -> List[Link]: ...
    def get_sections(self) -> List[Section]: ...
    def walk_links(self) -> list: ...

class Field:
    description: str
    example: Any
    location: str
    name: str
    required: Any
    schema: Any
    title: str
    def __init__(self, name: str, location: str, title: str = ..., description: str = ..., required: bool = ..., schema = ..., example = ...) -> None: ...

class Link:
    __doc__: str
    description: str
    encoding: str
    fields: list
    handler: Any
    method: str
    name: Any
    response: Any
    title: str
    url: str
    def __init__(self, url: str, method: str, handler: Optional[Callable] = ..., name: str = ..., encoding: str = ..., response: Optional[Response] = ..., title: str = ..., description: str = ..., fields: Optional[Sequence[Field]] = ...) -> None: ...
    def get_body_field(self) -> Any: ...
    def get_expanded_body(self) -> Any: ...
    def get_path_fields(self) -> list: ...
    def get_query_fields(self) -> list: ...

class Response:
    encoding: str
    schema: Any
    status_code: int
    def __init__(self, encoding: str, status_code: int = ..., schema = ...) -> None: ...

class Section:
    content: list
    description: str
    name: str
    title: str
    def __init__(self, name: str, content: Optional[Sequence[Union[Link, Section]]] = ..., title: str = ..., description: str = ...) -> None: ...
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
