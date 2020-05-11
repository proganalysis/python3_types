# (generated with --quick)

import typing
from typing import Dict, Tuple, Type
import weakref

Any: typing.Any
Clip: typing.Any
Environment: typing.Any
Feature: typing.Any
Frame: typing.Any
HasTraits: typing.Any
IPyImage: typing.Any
Image: typing.Any
Instance: typing.Any
Preview: typing.Any
WeakKeyDictionary: Type[weakref.WeakKeyDictionary]
default: typing.Any
observe: typing.Any

class Formatter(typing.Any):
    _default__cache: typing.Any
    cache: typing.Any
    display_formatters: typing.Any
    def deinitialize(self) -> None: ...
    def display(self, obj: typing.Any, *args, **kwargs) -> typing.Any: ...
    def initialize(self) -> None: ...
    def wrap_cached(self, obj: typing.Any) -> typing.Any: ...

class InlineFormat(typing.Any):
    REPR_TYPES: Dict[str, str]
    __doc__: str
    _default_preview: typing.Any
    _ipy_image_cache: typing.Any
    _update_initial_frame: typing.Any
    clip: typing.Any
    environment: typing.Any
    first_frame: typing.Any
    ipy_image: typing.Any
    preview: typing.Any
    def _repr_mimebundle_(self, include: typing.Any = ..., exclude: typing.Any = ...) -> Tuple[dict, dict]: ...
    def _repr_png(self, *args, **kwargs) -> typing.Any: ...
    def _repr_pretty(self) -> str: ...
    def _repr_preview(self) -> typing.Any: ...
