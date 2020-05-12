import tensorflow as tf
from neuralmonkey.dataset import Dataset as Dataset
from neuralmonkey.model.feedable import FeedDict as FeedDict
from neuralmonkey.model.model_part import ModelPart
from neuralmonkey.model.parameterized import InitializerSpecs as InitializerSpecs
from neuralmonkey.model.stateful import TemporalStateful
from neuralmonkey.vocabulary import Vocabulary as Vocabulary
from typing import Any, Dict, List

class Sequence(ModelPart, TemporalStateful):
    max_length: Any = ...
    def __init__(self, name: str, max_length: int=..., reuse: ModelPart=..., save_checkpoint: str=..., load_checkpoint: str=..., initializers: InitializerSpecs=...) -> None: ...

class EmbeddedFactorSequence(Sequence):
    vocabularies: Any = ...
    vocabulary_sizes: Any = ...
    data_ids: Any = ...
    embedding_sizes: Any = ...
    add_start_symbol: Any = ...
    add_end_symbol: Any = ...
    scale_embeddings_by_depth: Any = ...
    embeddings_source: Any = ...
    trainable: Any = ...
    def __init__(self, name: str, vocabularies: List[Vocabulary], data_ids: List[str], embedding_sizes: List[int], max_length: int=..., add_start_symbol: bool=..., add_end_symbol: bool=..., scale_embeddings_by_depth: bool=..., trainable: bool=..., embeddings_source: EmbeddedFactorSequence=..., reuse: ModelPart=..., save_checkpoint: str=..., load_checkpoint: str=..., initializers: InitializerSpecs=...) -> None: ...
    @property
    def input_types(self) -> Dict[str, tf.DType]: ...
    @property
    def input_shapes(self) -> Dict[str, tf.TensorShape]: ...
    def input_factor_indices(self) -> List[tf.Tensor]: ...
    def input_factors(self) -> List[tf.Tensor]: ...
    def embedding_matrices(self) -> List[tf.Tensor]: ...
    def temporal_states(self) -> tf.Tensor: ...
    def temporal_mask(self) -> tf.Tensor: ...
    def feed_dict(self, dataset: Dataset, train: bool=...) -> FeedDict: ...

class EmbeddedSequence(EmbeddedFactorSequence):
    def __init__(self, name: str, vocabulary: Vocabulary, data_id: str, embedding_size: int, max_length: int=..., add_start_symbol: bool=..., add_end_symbol: bool=..., scale_embeddings_by_depth: bool=..., trainable: bool=..., embeddings_source: EmbeddedSequence=..., reuse: ModelPart=..., save_checkpoint: str=..., load_checkpoint: str=..., initializers: InitializerSpecs=...) -> None: ...
    @property
    def inputs(self) -> tf.Tensor: ...
    @property
    def embedding_matrix(self) -> tf.Tensor: ...
    @property
    def vocabulary(self) -> Vocabulary: ...
    @property
    def data_id(self) -> str: ...
