# (generated with --quick)

from typing import Any, IO, List

_: Any
bz2: module
contextlib: module
count: int
dictionaries_loc: str
f: str
generate: Any
glob: module
log_it: Any
open_cache: Any
os: module
patrick_logger: Any
pickle: module
proper_nouns: List[str]
searcher: Any
shlex: module
subprocess: module
tests_performed: Any
tests_performed_cache_loc: str
tg: Any
th: Any
the_cache: IO
time: module

def __getattr__(name) -> Any: ...
def check_file(what_file: str) -> None: ...
def check_test_performed(text, test: str) -> bool: ...
def decapitalize_beginnings_of_lines(the_poem: List[str], poem_path: str) -> List[str]: ...
def get_first_word(line: str) -> str: ...
def load_proper_noun_data() -> List[str]: ...
def prompt_and_confirm(prompt: str) -> bool: ...
def set_test_performed(text, test: str) -> None: ...
def write_cache() -> None: ...
