# (generated with --quick)

from typing import Any, Dict, List, Pattern, Tuple

CONTENT_SIZE: int
FACTOR: int
KEYWORDS: Any
KEYWORDS_CACHE: Dict[str, Tuple[int, int]]
LOGGER: logging.Logger
SEPARATOR: Pattern[str]
SHIFT: int
SPECIAL_KEYWORDS: Dict[str, str]
config_dict: Any
logging: module
math: module
re: module

def _merge(hash_list: List[Tuple[int, int]]) -> Tuple[int, int]: ...
def _normalize(vector: List[int]) -> List[float]: ...
def _prepare_cache() -> Dict[str, Tuple[int, int]]: ...
def _vectorize(tokens: List[str]) -> List[int]: ...
def extract(text: str) -> List[float]: ...
def split(text: str) -> List[str]: ...
