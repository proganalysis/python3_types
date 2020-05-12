# (generated with --quick)

import collections
import familia_wrapper
from typing import Any, Optional, Pattern, Type

InferenceEngineWrapper: Type[familia_wrapper.InferenceEngineWrapper]
NotFound: Any
RE_BACKSPACES: Pattern[str]
Sanic: Any
TopicalWordEmbeddingsWrapper: Type[familia_wrapper.TopicalWordEmbeddingsWrapper]
api_distance: Any
api_index: Any
api_lda: Any
api_similarity_keywords: Any
api_similarity_query: Any
api_slda: Any
api_tokenize: Any
app: Any
defaultdict: Type[collections.defaultdict]
doc: Any
emb_file: str
ignore_404s: Any
inference_engine_lda: familia_wrapper.InferenceEngineWrapper
inference_engine_slda: familia_wrapper.InferenceEngineWrapper
json: Any
lda_topic_words: collections.defaultdict[int, list]
logger: Any
model_dir: str
model_name: str
multiprocessing: module
n_workers: int
nearest_words: Any
os: module
re: module
swagger_blueprint: Any
traceback: module
twe: familia_wrapper.TopicalWordEmbeddingsWrapper

def error_response(message = ...) -> Any: ...
def get_param(request, param_name, default_value = ..., is_list = ...) -> Any: ...
def handle_404(request, exception) -> Any: ...
def handle_exception(request, exception) -> Any: ...
def read_topic_words_from_file(topic_words_file_name = ...) -> collections.defaultdict[int, list]: ...
def response(success = ..., data = ..., message = ...) -> Any: ...
def strip_to_none(text) -> Optional[str]: ...
