# (generated with --quick)

from typing import Any, Optional, Type, TypeVar

Argument: Any
COMMENT_PATTERN: Any
COMMENT_SUB: Any
ENDING_WS_MATCH: Any
REVERSE: Any
SPACE_AFTER_SEARCH: Any
STARTING_WS_MATCH: Any
SubWikiTextWithArgs: Any
TL_NAME_ARGS_FULLMATCH: Any
WS: Any
regex_compile: Any

T = TypeVar('T')

class Template(Any):
    __doc__: str
    _first_arg_sep: int
    _name_args_matcher: Any
    def del_arg(self, name) -> None: ...
    def get_arg(self, name) -> Any: ...
    def has_arg(self, name, value = ...) -> bool: ...
    def normal_name(self, rm_namespaces = ..., capital_links = ..., _code = ..., *, code = ..., capitalize = ...) -> str: ...
    def rm_dup_args_safe(self, tag = ...) -> None: ...
    def rm_first_of_dup_args(self) -> None: ...
    def set_arg(self, name, value, positional = ..., before = ..., after = ..., preserve_spacing = ...) -> None: ...

def get_arg(name, args) -> Any: ...
def mode(list_) -> Any: ...
@overload
def warn(message: Warning, category = ..., stacklevel: int = ..., source = ...) -> None: ...
@overload
def warn(message: str, category: Optional[Type[Warning]] = ..., stacklevel: int = ..., source = ...) -> None: ...