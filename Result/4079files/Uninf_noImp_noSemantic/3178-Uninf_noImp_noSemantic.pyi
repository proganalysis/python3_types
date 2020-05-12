from typing import Any, Dict, List, NamedTuple, Optional, TypeVar, Union

def entropy(class_probabilities: List[float]) -> float: ...
def class_probabilities(labels: List[Any]) -> List[float]: ...
def data_entropy(labels: List[Any]) -> float: ...
def partition_entropy(subsets: List[List[Any]]) -> float: ...

class Candidate(NamedTuple):
    level: str
    lang: str
    tweets: bool
    phd: bool
    did_well: Optional[bool] = ...

inputs: Any
T = TypeVar('T')

def partition_by(inputs: List[T], attribute: str) -> Dict[Any, List[T]]: ...
def partition_entropy_by(inputs: List[Any], attribute: str, label_attribute: str) -> float: ...

senior_inputs: Any

class Leaf(NamedTuple):
    value: Any

class Split(NamedTuple):
    attribute: str
    subtrees: dict
    default_value: Any = ...
DecisionTree = Union[Leaf, Split]
hiring_tree: Any

def classify(tree: DecisionTree, input: Any) -> Any: ...
def build_tree_id3(inputs: List[Any], split_attributes: List[str], target_attribute: str) -> DecisionTree: ...

tree: Any
