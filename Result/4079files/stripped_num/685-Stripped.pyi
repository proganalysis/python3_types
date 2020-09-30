# (generated with --quick)

import aoareader.Dict
from typing import Any, Callable, Dict, Iterable, List, Tuple, Type, TypeVar

Parallel: Any
Vocabulary: Type[aoareader.Dict.Dict]
aoareader: module
argv: List[str]
data_filenames: Dict[str, str]
data_path: str
delayed: Any
dict_file: str
itertools: module
json: module
np: module
os: module
time: module
torch: Any
vocab_file: str
word_tokenize: Any

_S = TypeVar('_S')
_T = TypeVar('_T')

def build_dict(stories) -> aoareader.Dict.Dict: ...
def get_stories(story_lines, with_answer = ...) -> List[Tuple[Any, Any, Any, Any]]: ...
def main() -> None: ...
def parse_stories(lines, with_answer = ...) -> List[Tuple[list, Any, Any, list]]: ...
@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...
def tokenize(sentence) -> list: ...
def vectorize_stories(stories, vocab) -> Tuple[list, list, Any, list]: ...
