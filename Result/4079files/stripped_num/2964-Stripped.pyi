# (generated with --quick)

from typing import Any

Schema: Any
URIRef: Any
pyxb: Any

class PrefixMap:
    __doc__: str
    _map: dict
    _nsc: Any
    def __init__(self, schema, dom_schema) -> None: ...
    def namespaces(self) -> dict: ...
    def uri_for(self, iri) -> Any: ...
