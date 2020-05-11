# (generated with --quick)

from typing import Any, Dict, Iterable, List, Sequence, TypeVar

DataSource: Any
ENDING_PARENTHESIS_PATTERN: str
Keyword: Any
KeywordLabel: Any
re: module

_T = TypeVar('_T')

class KeywordMatcher(object):
    labels: dict_keys
    name_to_keyword_ids: Dict[Any, set]
    skip: bool
    def match(self, text) -> Any: ...

def get_close_matches(word: Sequence[_T], possibilities: Iterable[Sequence[_T]], n: int = ..., cutoff: float = ...) -> List[Sequence[_T]]: ...
