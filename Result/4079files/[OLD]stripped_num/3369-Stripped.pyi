# (generated with --quick)

from typing import Any, Callable, Dict, List, NoReturn, Tuple, TypeVar, Union

DictCallable: Any
Dispatch: Any
ListCallable: Any
Parallel: Any
SetCallable: Any
TupleCallable: Any
__all__: List[str]
builtins: module
complement: Any
compose: Any
delayed: Any
filter: Any
first: Any
identity: Any
juxt: Any
keyfilter: Any
last: Any
map: Any
merge: Any
operator: module
partial: Any
peek: Any
pipe: Any
second: Any
toolz: Any
valfilter: Any

_T0 = TypeVar('_T0')
_TChain = TypeVar('_TChain', bound=Chain)
_T_x = TypeVar('_T_x', bound=_x)

class Chain(ChainBase):
    _args: tuple
    _composer: DefaultComposer
    _dir: List[nothing]
    _kwargs: Dict[str, Any]
    _tokens: list
    compose: Any
    def __call__(self: _TChain, *args, **kwargs) -> _TChain: ...
    def __getattr__(self: _TChain, attr) -> _TChain: ...
    def __getitem__(self: _TChain, item) -> _TChain: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def compute(self, *args, **kwargs) -> Any: ...
    def copy(self, klass = ...) -> Any: ...

class ChainBase(object):
    def __dir__(self) -> Any: ...
    def _tokenize(self, composer, attr) -> Any: ...
    def compute(self, fn, *args, **kwargs) -> Any: ...

class ComposerBase(object):
    attrs: Any
    def __init__(self, **kwargs) -> None: ...

class DefaultComposer(ComposerBase):
    attrs: Any
    imports: list
    def attr(self, item) -> Any: ...
    def call(self, tokens: _T0, *args, **kwargs) -> _T0: ...
    def composer(self, tokens) -> Any: ...
    def item(self, item: _T0) -> _T0: ...

class LiterateAPI(chain):
    _args: tuple
    _kwargs: Dict[str, Any]
    _tokens: List[nothing]

class ParallelComposer(SugarComposer):
    n_jobs: Any
    def __init__(self, n_jobs = ...) -> None: ...
    def composer(self, tokens, **kwargs) -> Any: ...

class SugarComposer(DefaultComposer):
    attrs: Any
    multiple_dispatch: Any
    def call(self, tokens: _T0, *args, **kwargs) -> _T0: ...
    def item(self, item) -> Any: ...

class ThisComposer(DefaultComposer):
    attrs: Any
    def attr(self, item: _T0) -> List[List[Union[Callable[[Any, Any], Any], Dict[nothing, nothing], List[_T0]]]]: ...
    def call(self, tokens: _T0, *args, **kwargs) -> _T0: ...
    def item(self, item: _T0) -> List[List[Union[Callable[[Any, Any], Any], Dict[nothing, nothing], List[_T0]]]]: ...

class __p(__x):
    _args: tuple
    _composer: ParallelComposer
    _kwargs: Dict[str, Any]
    _tokens: List[nothing]
    def __init__(self, *args, n_jobs = ..., **kwargs) -> None: ...

class __x(_x):
    _args: tuple
    _kwargs: Dict[str, Any]
    _tokens: List[nothing]
    def _(self, *args, **kwargs) -> NoReturn: ...

class _this(_x):
    __dir__: Any
    __doc__: str
    _args: Tuple[Any]
    _composer: ThisComposer
    _kwargs: Dict[nothing, nothing]
    _tokens: Any
    def __init__(self, arg = ...) -> None: ...

class _x(LiterateAPI):
    __doc__: str
    _args: tuple
    _composer: SugarComposer
    _kwargs: Dict[str, Any]
    _tokens: Any
    def __add__(self: _T_x, f) -> _T_x: ...
    def __gt__(self, f) -> Any: ...
    def __mul__(self: _T_x, f) -> _T_x: ...
    def __or__(self: _T_x, f) -> _T_x: ...

class chain(Chain):
    _args: tuple
    _kwargs: Dict[str, Any]
    _tokens: List[nothing]
    def __repr__(self) -> Any: ...

def evaluate(args, kwargs, fn) -> Any: ...
def getattr_(item, obj) -> Any: ...
def getitem(item, obj) -> Any: ...
def juxtapose(func, x) -> Any: ...
