# (generated with --quick)

import collections
import itertools
from typing import Any, Tuple, Type, TypeVar

chain: Type[itertools.chain]
defaultdict: Type[collections.defaultdict]
logger: logging.Logger
logging: module
nx: module
utils: Any

AnyStr = TypeVar('AnyStr', str, bytes)

def build(recipes, config, blacklist = ..., restrict = ...) -> Tuple[Any, collections.defaultdict]: ...
def build_from_recipes(recipes) -> Any: ...
def filter(dag, packages) -> Any: ...
def filter_recipe_dag(dag, include, exclude) -> Any: ...
def fnmatch(name: AnyStr, pat: AnyStr) -> bool: ...
