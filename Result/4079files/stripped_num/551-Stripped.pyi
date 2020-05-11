# (generated with --quick)

import __builtin__
import __future__
import builtins
from typing import Any, Type

Analysis: Any
UnderlyingAnalysis: Any
absolute_import: __future__._Feature
division: __future__._Feature
print_function: __future__._Feature
str: Type[builtins.str]
text_type: Any
unicode_literals: __future__._Feature

class ZincAnalysis(Any):
    FORMAT_VERSION_LINE: Any
    __doc__: __builtin__.str
    _underlying_analysis: Any
    underlying_analysis: Any
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, underlying_analysis) -> None: ...
    def __ne__(self, other) -> bool: ...
    def __str__(self) -> Any: ...
    def __unicode__(self) -> Any: ...
    def write(self, outfile) -> None: ...
