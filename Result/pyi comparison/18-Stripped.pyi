# (generated with --quick)

import collections
import contextlib
from typing import Any, List, Set, Type

KrakenRepoException: Any
MODEL_REPO: str
SUPPORTED_MODELS: Set[str]
__all__: List[str]
closing: Type[contextlib.closing]
defaultdict: Type[collections.defaultdict]
json: module
logger: logging.Logger
logging: module
os: module
requests: module
urllib: module

def get_description(model_id, callback = ...) -> Any: ...
def get_listing(callback = ...) -> dict: ...
def get_model(model_id, path, callback = ...) -> Any: ...
def publish_model(model_file = ..., metadata = ..., access_token = ..., callback = ...) -> Any: ...
