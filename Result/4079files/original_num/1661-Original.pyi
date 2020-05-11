# (generated with --quick)

from typing import Any, Type, TypeVar

gettext: module

_T_ = TypeVar('_T_', bound=_)

class _(str):
    lang: Any
    observers: set
    source_text: Any
    def __new__(cls: Type[_T_], s) -> _T_: ...
    @staticmethod
    def bind(label) -> None: ...
    @staticmethod
    def switch_lang(lang) -> None: ...
    @staticmethod
    def translate(s, *args, **kwargs) -> Any: ...
