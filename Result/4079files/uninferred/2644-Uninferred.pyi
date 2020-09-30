from Stats.Stats import Stats
from typing import Any, Dict, List, TypeVar

PandasDataFrame = TypeVar('DataFrame')
SklearnRandomForestClassifier = TypeVar('RandomForestClassifier')
__author__: str
__copyright__: str
__credits__: Any
__license__: str
__version__: str
__maintainer__: str
__email__: str
__status__: str

class _RandomForestClassifier(Stats):
    def __init__(self) -> None: ...
    def train(self, features_indep_df: PandasDataFrame, feature_target: List, model_labals: List=..., **kwargs: Any) -> SklearnRandomForestClassifier: ...
    def train_summaries(self, model_train: SklearnRandomForestClassifier) -> Dict: ...
    def plot(self, model_train: SklearnRandomForestClassifier, feature_names: List, class_names: List=...) -> Any: ...
