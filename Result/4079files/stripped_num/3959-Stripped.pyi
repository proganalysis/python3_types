# (generated with --quick)

import collections
import typing
from typing import Type, TypeVar

Mapping: Type[typing.Mapping]
OrderedDict: Type[collections.OrderedDict]
odict: OrderedDictMaker

_T0 = TypeVar('_T0')

class OrderedDictMaker(object):
    __doc__: str
    def __getitem__(self, keys) -> collections.OrderedDict: ...

def update_dict(dst: _T0, src) -> _T0: ...
