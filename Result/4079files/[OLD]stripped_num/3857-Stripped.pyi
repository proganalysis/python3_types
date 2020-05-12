# (generated with --quick)

import datetime
from typing import Any, Type

OptionQuery: Any
OptionStrategy: Any
OptionType: Any
Period: Any
pd: Any
timedelta: Type[datetime.timedelta]

class OptionStrategies(object):
    __doc__: str
    @staticmethod
    def back_ratio(chain, **params) -> None: ...
    @staticmethod
    def butterfly(chain, **params) -> None: ...
    @staticmethod
    def calendar(chain, **params) -> Any: ...
    @staticmethod
    def combo(chain, **params) -> None: ...
    @staticmethod
    def condor(chain, **params) -> None: ...
    @staticmethod
    def covered_stock(chain, **params) -> Any: ...
    @staticmethod
    def custom(chain, **params) -> None: ...
    @staticmethod
    def diagonal(chain, **params) -> None: ...
    @staticmethod
    def double_diagonal(chain, **params) -> None: ...
    @staticmethod
    def iron_condor(chain, **params) -> Any: ...
    @staticmethod
    def single(chain, **params) -> Any: ...
    @staticmethod
    def straddle(chain, **params) -> None: ...
    @staticmethod
    def strangle(chain, **params) -> None: ...
    @staticmethod
    def vertical(chain, **params) -> Any: ...

def construct(symbol, strategy, chains, **kwargs) -> Any: ...
