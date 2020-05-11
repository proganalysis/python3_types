# (generated with --quick)

import collections
import typing
from typing import Any, Iterable, List, Mapping, Set, Tuple, Type

ANNOTATIONS: Any
BELGraph: Any
BELSyntaxError: Any
Counter: Type[typing.Counter]
MissingNamespaceNameWarning: Any
MissingNamespaceRegexWarning: Any
NakedNameWarning: Any
WarningTuple: Any
__all__: List[str]
defaultdict: Type[collections.defaultdict]
edge_has_annotation: Any
typing: module

def _iterate_namespace_name(graph) -> Iterable[Tuple[str, str]]: ...
def _naked_names_iter(graph) -> Iterable[str]: ...
def calculate_error_by_annotation(graph, annotation: str) -> Mapping[str, List[str]]: ...
def calculate_incorrect_name_dict(graph) -> Mapping[str, List[str]]: ...
def count_error_types(graph) -> typing.Counter[str]: ...
def count_naked_names(graph) -> typing.Counter[str]: ...
def get_naked_names(graph) -> Set[str]: ...
def get_syntax_errors(graph) -> list: ...
