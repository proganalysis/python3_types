# (generated with --quick)

import __builtin__
import __future__
import builtins
import collections
from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar, Union

absolute_import: __future__._Feature
deprecated: Any
division: __future__._Feature
is_list_option: Any
newstr: Any
object: Type[builtins.object]
print_function: __future__._Feature
str: Type[builtins.str]
unicode_literals: __future__._Feature

_Tnamedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices = TypeVar('_Tnamedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices', bound=`namedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices`)
_Tnamedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced = TypeVar('_Tnamedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced', bound=`namedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced`)

class HelpInfoExtracter(builtins.object):
    __doc__: __builtin__.str
    _scope: Any
    _scope_prefix: Any
    def __init__(self, scope) -> None: ...
    @staticmethod
    def compute_default(kwargs) -> Any: ...
    @staticmethod
    def compute_metavar(kwargs) -> Any: ...
    def get_option_help_info(self, args, kwargs) -> OptionHelpInfo: ...
    def get_option_scope_help_info(self, option_registrations_iter) -> OptionScopeHelpInfo: ...
    @classmethod
    def get_option_scope_help_info_from_parser(cls, parser) -> Any: ...

class OptionHelpInfo(`namedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices`):
    __doc__: __builtin__.str
    def comma_separated_display_args(self) -> __builtin__.str: ...

class OptionScopeHelpInfo(`namedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced`):
    __doc__: __builtin__.str

class `namedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices`(tuple):
    __slots__ = ["choices", "default", "deprecated_message", "display_args", "help", "registering_class", "removal_hint", "removal_version", "scoped_cmd_line_args", "typ", "unscoped_cmd_line_args"]
    __dict__: collections.OrderedDict[__builtin__.str, Any]
    _fields: Tuple[__builtin__.str, __builtin__.str, __builtin__.str, __builtin__.str, __builtin__.str, __builtin__.str, __builtin__.str, __builtin__.str, __builtin__.str, __builtin__.str, __builtin__.str]
    choices: Any
    default: Any
    deprecated_message: Any
    display_args: Any
    help: Any
    registering_class: Any
    removal_hint: Any
    removal_version: Any
    scoped_cmd_line_args: Any
    typ: Any
    unscoped_cmd_line_args: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices`], registering_class, display_args, scoped_cmd_line_args, unscoped_cmd_line_args, typ, default, help, deprecated_message, removal_version, removal_hint, choices) -> `_Tnamedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices`: ...
    def _asdict(self) -> collections.OrderedDict[__builtin__.str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices`: ...
    def _replace(self: `_Tnamedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices`, **kwds) -> `_Tnamedtuple-_OptionHelpInfo-registering_class-display_args-scoped_cmd_line_args-unscoped_cmd_line_args-typ-default-help-deprecated_message-removal_version-removal_hint-choices`: ...

class `namedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced`(tuple):
    __slots__ = ["advanced", "basic", "recursive", "scope"]
    __dict__: collections.OrderedDict[__builtin__.str, Any]
    _fields: Tuple[__builtin__.str, __builtin__.str, __builtin__.str, __builtin__.str]
    advanced: Any
    basic: Any
    recursive: Any
    scope: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced`], scope, basic, recursive, advanced) -> `_Tnamedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced`: ...
    def _asdict(self) -> collections.OrderedDict[__builtin__.str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced`: ...
    def _replace(self: `_Tnamedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced`, **kwds) -> `_Tnamedtuple-_OptionScopeHelpInfo-scope-basic-recursive-advanced`: ...

def namedtuple(typename: __builtin__.str, field_names: Union[__builtin__.str, Iterable[__builtin__.str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
