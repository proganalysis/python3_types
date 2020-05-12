# (generated with --quick)

from typing import Any

np: module

class VaR(object):
    _VaR__alpha: Any
    _VaR__losses: Any
    _VaR__series: Any
    _VaR__tail: Any
    cvar: Any
    var: Any
    def __init__(self, series, alpha = ...) -> None: ...

def cvar(series, alpha = ...) -> Any: ...
def var(series, alpha = ...) -> Any: ...
