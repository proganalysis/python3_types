# (generated with --quick)

from typing import Any, Dict, List, Pattern, Tuple

CONTENT_SIZE: int
FACTOR: int
KEYWORDS: Any
KEYWORDS_CACHE: Dict[Any, Tuple[Any, int]]
LOGGER: logging.Logger
SEPARATOR: Pattern[str]
SHIFT: int
SPECIAL_KEYWORDS: Dict[str, str]
config_dict: Any
logging: module
math: module
re: module

def _merge(hash_list) -> Tuple[Any, Any]: ...
def _normalize(vector) -> list: ...
def _prepare_cache() -> Dict[Any, Tuple[Any, int]]: ...
def _vectorize(tokens) -> list: ...
def extract(text) -> Any: ...
def split(text) -> List[str]: ...
