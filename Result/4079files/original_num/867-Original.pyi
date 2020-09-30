# (generated with --quick)

import lib.harvester
from typing import Any, Dict, Type, TypeVar, Union

BNode: Any
CRM: Any
DC: Any
DCTERMS: Any
FOAF: Any
GAZ_ID: Any
GEO: Any
Graph: Any
Harvester: Type[lib.harvester.Harvester]
Literal: Any
Namespace: Any
NamespaceManager: Any
OWL: Any
RDF: Any
RDFS: Any
SF: Any
SKOS: Any
URIRef: Any
WGS84_POS: Any
XSI: Any
argparse: module
data: Any
formatter: logging.Formatter
harvester: lib.harvester.Harvester
logger: logging.Logger
logging: module
namespace_manager: Any
options: Dict[str, Any]
parser: argparse.ArgumentParser
pycountry: Any
rdf_graph: Any

_T0 = TypeVar('_T0')

def create_awk_multipolygon(multipolygon) -> str: ...
def create_place_rdf(graph: _T0, place) -> _T0: ...
def create_rdf(places) -> Any: ...
def is_writable_directory(path: str) -> str: ...
@overload
def quote(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
