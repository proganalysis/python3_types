# (generated with --quick)

from typing import Any, List, TypeVar

Stats: Any
__author__: str
__copyright__: str
__credits__: List[str]
__email__: str
__license__: str
__maintainer__: str
__status__: str
__version__: str
sm: Any
sys: module

DataFrame = TypeVar('DataFrame')
MixedLM = TypeVar('MixedLM')
PandasDataFrame = TypeVar('PandasDataFrame')
StatsmodelsMixedLM = TypeVar('StatsmodelsMixedLM')

class _MixedLinearModel(Any):
    def __init__(self) -> None: ...
    def plot(self, model_train: MixedLM, feature_names: list, class_names: list = ...) -> None: ...
    def train(self, features_indep_df: DataFrame, feature_target: list, model_labals: list = ..., **kwargs) -> MixedLM: ...
    def train_summaries(self, model_train: MixedLM) -> dict: ...
