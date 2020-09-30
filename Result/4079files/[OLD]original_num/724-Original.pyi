# (generated with --quick)

import argparse
import pathlib
from typing import Any, List, Type

Namespace: Type[argparse.Namespace]
OntId: Any
OntTerm: Any
Path: Type[pathlib.Path]
devconfig: Any
embed: Any
json: module
makeGraph: Any
qname: Any
yaml: module

def convert_view_text_to_dict() -> dict: ...
def get_curies_from_scigraph_label_query(label: str, prefixes: List[str] = ...) -> list: ...
def linearize_graph(dict_: dict, tier_level: int = ...) -> tuple: ...
def main() -> None: ...
def normalize_term(term, prefix = ...) -> list: ...
def pair_terms(terms) -> List[argparse.Namespace]: ...
