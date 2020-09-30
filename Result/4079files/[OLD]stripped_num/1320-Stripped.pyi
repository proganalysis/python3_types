# (generated with --quick)

from typing import Any

DataSets: Any
GainRanking: Any
LabeledTree: Any
data_pd: Any
id3_credit: ID3
id3_tennis: ID3
pd_credit: Any

class ID3:
    class_name: Any
    ranking: Any
    tree: Any
    def __init__(self, training_set, class_name, ranking = ...) -> None: ...
    def __str__(self) -> str: ...
    def generate_tree(self, data_pd) -> Any: ...
