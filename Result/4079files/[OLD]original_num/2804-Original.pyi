# (generated with --quick)

from typing import Any, Tuple

Edge1HotFeatures: Any
EdgeBooleanFeatures: Any
EdgeNumericalSelector: Any
EdgeTransformerLogit: Any
FeatureDefinition: Any
FeatureUnion: Any
Node1HotFeatures: Any
NodeTransformerLogit: Any
NodeTransformerNeighbors: Any
NodeTransformerTextLen: Any
NodeTransformerXYWH: Any
PageNumberSimpleSequenciality: Any
Pipeline: Any
StandardScaler: Any

class FeatureDefinition_PageXml_LogitExtractor(Any):
    __doc__: str
    _edge_transformer: Any
    _node_transf_logit: Any
    _node_transformer: Any
    b_edge_lc: Any
    b_node_lc: Any
    n_feat_edge: Any
    n_feat_node: Any
    nbClass: Any
    t_ngrams_edge: Any
    t_ngrams_node: Any
    def __init__(self, nbClass = ..., n_feat_node = ..., t_ngrams_node = ..., b_node_lc = ..., n_feat_edge = ..., t_ngrams_edge = ..., b_edge_lc = ..., n_jobs = ...) -> None: ...
    def cleanTransformers(self) -> Tuple[Any, Any]: ...
    def fitTranformers(self, lGraph) -> bool: ...
    def getTransformers(self) -> Tuple[Any, Any]: ...
