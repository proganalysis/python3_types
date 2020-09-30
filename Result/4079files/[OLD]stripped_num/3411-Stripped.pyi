# (generated with --quick)

import string
from typing import Any, Pattern, Tuple, Type, TypeVar

Template: Type[string.Template]
doctest: module
re: module

_TInlineToken = TypeVar('_TInlineToken', bound=InlineToken)

class InlineToken(object):
    DEFAULT_STYLE: str
    DEFAULT_TEMPLATE: str
    NON_WORDS_RE: Pattern[str]
    __doc__: str
    image: Any
    style: str
    tag: Any
    template: string.Template
    title: Any
    def __init__(self, title, image = ..., style = ..., template = ..., tag = ...) -> None: ...
    def __str__(self) -> Any: ...
    def clone(self: _TInlineToken) -> _TInlineToken: ...
    def expand(self) -> str: ...
    def expand_in_string(self, str) -> Any: ...
    def needs_sandbox(self) -> bool: ...

def expand_inline_tokens(tokens, content) -> Tuple[list, bool]: ...
