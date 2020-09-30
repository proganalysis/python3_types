# (generated with --quick)

from typing import Any, Iterable

PackageFactory: Any
PackageMaker: Any
PackageTransformer: Any
Parser: Any
iter_xml_elements_at_level: Any

class SolusIndexParser(Any):
    def iter_parse(self, path: str, factory, transformer) -> Iterable: ...

def _expand_multiline_licenses(text: str) -> Iterable[str]: ...
