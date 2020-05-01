# (generated with --quick)

from typing import Any, List, TypeVar

__author__: str
__copyright__: str
__credits__: List[str]
__email__: str
__license__: str
__maintainer__: str
__status__: str
__version__: str
itemfreq: Any
np: module
statistics: module

NumpyNdarray = TypeVar('NumpyNdarray')
PandasDataFrame = TypeVar('PandasDataFrame')
ndarray = TypeVar('ndarray')

class FeatureParserThread:
    @staticmethod
    def aggregate_cell(postfixes: str, variable_type: str, prevalence: dict, variable_cell: str) -> ndarray: ...
    @staticmethod
    def prevalence_cell(variable_cell: str) -> list: ...
