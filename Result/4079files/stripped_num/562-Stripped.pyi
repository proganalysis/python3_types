# (generated with --quick)

import numpy
from typing import Any, Optional, Type, TypeVar, Union

CompilerWarning: Any
TransitModel: Any
atleast_2d: Any
cl: Any
float32: Any
int32: Any
ndarray: Type[numpy.ndarray]
np: module
ones: Any
squeeze: Any
uint32: Any
unique: Any
warnings: module
zeros: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class QPower2ModelCL(Any):
    __doc__: str
    _b_etimes: Any
    _b_f: Any
    _b_lcids: Any
    _b_nsamples: Any
    _b_p: Any
    _b_pbids: Any
    _b_time: Any
    _b_u: Any
    _time_id: None
    ctx: Any
    exptimes: Any
    f: Any
    lcids: Any
    nlc: Any
    npb: Any
    nptb: Any
    npv: Any
    nsamples: Any
    pbids: Any
    prg: Any
    pv: Any
    queue: Any
    spv: Any
    time: Optional[numpy.ndarray]
    u: Any
    def __init__(self, method = ..., is_secondary = ..., cl_ctx = ..., cl_queue = ...) -> None: ...
    def evaluate_ps(self, k, ldc, t0, p, a, i, e = ..., w = ..., copy = ...) -> Any: ...
    def evaluate_pv(self, pvp, ldc, copy = ...) -> Any: ...
    def set_data(self, time, lcids = ..., pbids = ..., nsamples = ..., exptimes = ...) -> None: ...

def array(object, dtype = ..., copy: bool = ..., order: str = ..., subok: bool = ..., ndmin: int = ...) -> numpy.ndarray: ...
def asarray(a, dtype = ..., order: Optional[str] = ...) -> numpy.ndarray: ...
def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
