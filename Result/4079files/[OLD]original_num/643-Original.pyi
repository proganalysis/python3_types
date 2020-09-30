# (generated with --quick)

import collections
from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar, Union

Link = `namedtuple-Link-text-url`

FilterExpression: Any
app_config: Any
apps: Any
breadcrumb: Any
connect: Any
core_markdown: Any
cuttrailing: Any
defaultfilters: Any
django_html: Any
do_loadmacros: Any
do_macro: Any
do_usemacro: Any
dropdown: Any
endswith: Any
field: Any
field_checkbox: Any
filename: Any
fragments: Any
full_url: Any
get: Any
get_assets: Any
get_parameters: Any
get_template: Any
html: module
html2text: Any
include_assets: Any
include_features: Any
include_fragments: Any
json: module
limit: Any
link: Any
link_to: Any
markdown: Any
menu: Any
nolinebreaks: Any
os: module
override: Any
pagination: Any
python_bleach: module
python_html2text: Any
python_markdown: Any
random: module
random_item: Any
ref: Any
register: Any
render_app_config: Any
safestring: Any
settings: Any
sites_models: Any
startswith: Any
template: Any
time: Any
toc: Any
url_for_user: Any

_Tnamedtuple-Link-text-url = TypeVar('_Tnamedtuple-Link-text-url', bound=`namedtuple-Link-text-url`)

class DefineMacroNode(Any):
    args: Any
    kwargs: Any
    name: Any
    nodelist: Any
    def __init__(self, name, nodelist, args) -> None: ...
    def render(self, context) -> str: ...

class DropdownNode(Any):
    label: Any
    name: Any
    nodelist: Any
    def __init__(self, name, label, nodelist) -> None: ...
    def render(self, context) -> Any: ...

class LoadMacrosNode(Any):
    def render(self, context) -> str: ...

class UseMacroNode(Any):
    fe_args: Any
    fe_kwargs: Any
    macro: Any
    def __init__(self, macro, fe_args, fe_kwargs) -> None: ...
    def render(self, context) -> Any: ...

class `namedtuple-Link-text-url`(tuple):
    __slots__ = ["text", "url"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str]
    text: Any
    url: Any
    def __getnewargs__(self) -> Tuple[Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Link-text-url`], text, url) -> `_Tnamedtuple-Link-text-url`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Link-text-url`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Link-text-url`: ...
    def _replace(self: `_Tnamedtuple-Link-text-url`, **kwds) -> `_Tnamedtuple-Link-text-url`: ...

def _setup_macros_dict(parser) -> None: ...
def bleach(text, disable_tags = ..., except_for = ...) -> Any: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def parse_token_args(args, filterval = ...) -> Tuple[list, dict]: ...
