# (generated with --quick)

import collections
import typing
from typing import Any, Generator, List, Tuple, Type

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

def _iterate_namespace_name(graph) -> Generator[Tuple[Any, Any], Any, None]: ...
def _naked_names_iter(graph) -> Generator[Any, Any, None]: ...
def calculate_error_by_annotation(graph, annotation) -> dict: ...
def calculate_incorrect_name_dict(graph) -> dict: ...
def count_error_types(graph) -> typing.Counter[nothing]: ...
def count_naked_names(graph) -> typing.Counter[nothing]: ...
def get_naked_names(graph) -> set: ...
def get_syntax_errors(graph) -> List[Tuple[Any, Any, Any]]: ...
