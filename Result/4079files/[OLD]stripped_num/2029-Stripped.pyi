# (generated with --quick)

from typing import Any, List

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
    add_end_symbol: Any
    add_start_symbol: Any
    data_ids: Any
    embedding_matrices: Any
    embedding_sizes: Any
    embeddings_source: Any
    input_factor_indices: Any
    input_factors: Any
    input_shapes: dict
    input_types: dict
    max_length: Any
    scale_embeddings_by_depth: Any
    temporal_mask: Any
    temporal_states: Any
    trainable: Any
    vocabularies: Any
    vocabulary_sizes: List[int]
    def __init__(self, name, vocabularies, data_ids, embedding_sizes, max_length = ..., add_start_symbol = ..., add_end_symbol = ..., scale_embeddings_by_depth = ..., trainable = ..., embeddings_source = ..., reuse = ..., save_checkpoint = ..., load_checkpoint = ..., initializers = ...) -> None: ...
    def feed_dict(self, dataset, train = ...) -> Any: ...

class EmbeddedSequence(EmbeddedFactorSequence):
    __doc__: str
    add_end_symbol: Any
    add_start_symbol: Any
    data_id: Any
    data_ids: list
    embedding_matrix: Any
    embedding_sizes: list
    embeddings_source: Any
    inputs: Any
    max_length: Any
    scale_embeddings_by_depth: Any
    trainable: Any
    vocabularies: list
    vocabulary: Any
    vocabulary_sizes: Any
    def __init__(self, name, vocabulary, data_id, embedding_size, max_length = ..., add_start_symbol = ..., add_end_symbol = ..., scale_embeddings_by_depth = ..., trainable = ..., embeddings_source = ..., reuse = ..., save_checkpoint = ..., load_checkpoint = ..., initializers = ...) -> None: ...

class Sequence(Any, Any):
    __doc__: str
    max_length: Any
    def __init__(self, name, max_length = ..., reuse = ..., save_checkpoint = ..., load_checkpoint = ..., initializers = ...) -> None: ...
