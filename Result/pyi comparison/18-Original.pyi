# (generated with --quick)

import collections
import contextlib
from typing import Any, BinaryIO, Callable, List, Optional, Set, Type

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

def get_description(model_id: str, callback: Callable = ...) -> dict: ...
def get_listing(callback: Callable = ...) -> dict: ...
def get_model(model_id: str, path: str, callback: Callable = ...) -> str: ...
def publish_model(model_file: Optional[BinaryIO] = ..., metadata: Optional[dict] = ..., access_token: Optional[str] = ..., callback: Callable = ...) -> str: ...
