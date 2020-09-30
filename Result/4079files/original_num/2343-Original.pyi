# (generated with --quick)

import collections
from typing import Any, Generator, List, Tuple, Type, TypeVar

OrderedDict: Type[collections.OrderedDict]
defaultdict: Type[collections.defaultdict]
logger: logging.Logger
logging: module

_T0 = TypeVar('_T0')

class Form(object):
    level: Any
    prefixes: List[nothing]
    rule: Any
    spec: Any
    stem: Any
    suffixes: List[nothing]
    def __init__(self, rule, spec, level, stem = ...) -> None: ...
    def get_word(self, stem) -> str: ...

class Grammar(object):
    hs: Any
    rules: Any
    stems: collections.defaultdict
    suffixes: List[Tuple[Any, Any]]
    tree: Any
    def __init__(self, hs, tree, rules) -> None: ...
    def check_spelling(self, words) -> bool: ...
    def create_indexes(self, rules) -> Tuple[collections.defaultdict, List[Tuple[Any, Any]]]: ...
    def find_rules(self, word: _T0) -> Generator[Tuple[Any, Any, Any], Any, None]: ...
    def iter_rules(self, word) -> Generator[Tuple[Word, Word], Any, None]: ...

class Rule(object):
    forms: collections.OrderedDict[nothing, nothing]
    includes: collections.defaultdict[nothing, list]
    key: Any
    lineno: Any
    macro: Any
    name: Any
    def __init__(self, lineno, key, name, macro = ...) -> None: ...
    def __str__(self) -> Any: ...
    def build_forms(self, stem) -> Generator[nothing, Any, None]: ...
    def match(self, word) -> None: ...

class Word(object):
    form: Any
    stem: Any
    def __init__(self, form, stem) -> None: ...
    def __str__(self) -> Any: ...

def change_spec(symbols, spec, **kwargs) -> str: ...
def check_spec(symbols, spec, **kwargs) -> bool: ...
def get_properties(symbols, spec) -> collections.OrderedDict: ...
