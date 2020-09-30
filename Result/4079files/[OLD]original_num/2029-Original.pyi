# (generated with --quick)

from typing import Any, Dict, List, Optional

Dataset: Any
FeedDict: Any
InitializerSpecs: Any
ModelPart: Any
TemporalStateful: Any
Vocabulary: Any
check_argument_types: Any
get_variable: Any
pad_batch: Any
sentence_mask: Any
tensor: Any
tf: Any

class EmbeddedFactorSequence(Sequence):
    __doc__: str
    add_end_symbol: bool
    add_start_symbol: bool
    data_ids: List[str]
    embedding_matrices: Any
    embedding_sizes: List[int]
    embeddings_source: Any
    input_factor_indices: Any
    input_factors: Any
    input_shapes: Dict[str, Any]
    input_types: Dict[str, Any]
    max_length: Any
    scale_embeddings_by_depth: bool
    temporal_mask: Any
    temporal_states: Any
    trainable: bool
    vocabularies: list
    vocabulary_sizes: Any
    def __init__(self, name: str, vocabularies: list, data_ids: List[str], embedding_sizes: List[int], max_length: Optional[int] = ..., add_start_symbol: bool = ..., add_end_symbol: bool = ..., scale_embeddings_by_depth: bool = ..., trainable: bool = ..., embeddings_source: Optional[EmbeddedFactorSequence] = ..., reuse = ..., save_checkpoint: Optional[str] = ..., load_checkpoint: Optional[str] = ..., initializers = ...) -> None: ...
    def feed_dict(self, dataset, train: bool = ...) -> Any: ...

class EmbeddedSequence(EmbeddedFactorSequence):
    __doc__: str
    add_end_symbol: bool
    add_start_symbol: bool
    data_id: str
    data_ids: List[str]
    embedding_matrix: Any
    embedding_sizes: List[int]
    embeddings_source: Any
    inputs: Any
    max_length: Any
    scale_embeddings_by_depth: bool
    trainable: bool
    vocabularies: list
    vocabulary: Any
    vocabulary_sizes: Any
    def __init__(self, name: str, vocabulary, data_id: str, embedding_size: int, max_length: Optional[int] = ..., add_start_symbol: bool = ..., add_end_symbol: bool = ..., scale_embeddings_by_depth: bool = ..., trainable: bool = ..., embeddings_source: Optional[EmbeddedSequence] = ..., reuse = ..., save_checkpoint: Optional[str] = ..., load_checkpoint: Optional[str] = ..., initializers = ...) -> None: ...

class Sequence(Any, Any):
    __doc__: str
    max_length: Optional[int]
    def __init__(self, name: str, max_length: Optional[int] = ..., reuse = ..., save_checkpoint: Optional[str] = ..., load_checkpoint: Optional[str] = ..., initializers = ...) -> None: ...
