# (generated with --quick)

from typing import Any, Callable, IO, List, Set, TypeVar, Union

_: Any
bz2: module
contextlib: module
count: int
dictionaries_loc: str
f: str
generate: Any
glob: module
log_it: Any
open_cache: Callable[..., contextlib._GeneratorContextManager]
os: module
patrick_logger: Any
pickle: module
proper_nouns: Union[List[nothing], Set[str]]
searcher: Any
shlex: module
subprocess: module
tests_performed: Any
tests_performed_cache_loc: str
tg: Any
th: Any
the_cache: IO
time: module

_T0 = TypeVar('_T0')

def __getattr__(name) -> Any: ...
def check_file(what_file) -> None: ...
def check_test_performed(text, test) -> bool: ...
def decapitalize_beginnings_of_lines(the_poem: _T0, poem_path) -> _T0: ...
def get_first_word(line) -> Any: ...
def load_proper_noun_data() -> Set[str]: ...
def prompt_and_confirm(prompt) -> bool: ...
def set_test_performed(text, test) -> None: ...
def write_cache() -> None: ...
