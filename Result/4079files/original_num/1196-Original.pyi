# (generated with --quick)

from typing import Any, Iterable, List, Mapping, Optional

BELGraph: Any
DATETIME_FMT: str
DATE_FMT: str
DATE_VERSION_FMT: str
DEFAULT_NS_DESCRIPTION: str
__all__: List[str]
get_bel_resource: Any
get_incorrect_names_by_namespace: Any
get_names_by_namespace: Any
get_undefined_namespace_names: Any
log: logging.Logger
logging: module
os: module
write_namespace: Any

def export_namespace(graph, namespace: str, directory: Optional[str] = ..., cacheable: bool = ...) -> None: ...
def export_namespaces(graph, namespaces: Iterable[str], directory: Optional[str] = ..., cacheable: bool = ...) -> None: ...
def get_merged_namespace_names(locations: Iterable[str], check_keywords: bool = ...) -> Mapping[str, str]: ...
def merge_namespaces(input_locations, output_path, namespace_name, namespace_keyword, namespace_domain, author_name, citation_name, namespace_description = ..., namespace_species = ..., namespace_version = ..., namespace_query_url = ..., namespace_created = ..., author_contact = ..., author_copyright = ..., citation_description = ..., citation_url = ..., citation_version = ..., citation_date = ..., case_sensitive = ..., delimiter = ..., cacheable = ..., check_keywords = ...) -> None: ...
