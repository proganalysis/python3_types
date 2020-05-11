# (generated with --quick)

from typing import Any, Generator, List, TypeVar

Stats: Any
__author__: str
__copyright__: str
__credits__: List[str]
__email__: str
__license__: str
__maintainer__: str
__status__: str
__version__: str
ensemble: Any
pydotplus: Any
tree: Any

DataFrame = TypeVar('DataFrame')
PandasDataFrame = TypeVar('PandasDataFrame')
RandomForestClassifier = TypeVar('RandomForestClassifier')
SklearnRandomForestClassifier = TypeVar('SklearnRandomForestClassifier')

class _RandomForestClassifier(Any):
    def __init__(self) -> None: ...
    def plot(self, model_train: RandomForestClassifier, feature_names: list, class_names: list = ...) -> Generator[Any, Any, None]: ...
    def train(self, features_indep_df: DataFrame, feature_target: list, model_labals: list = ..., **kwargs) -> RandomForestClassifier: ...
    def train_summaries(self, model_train: RandomForestClassifier) -> dict: ...
