from repology.packagemaker import PackageFactory, PackageMaker as PackageMaker
from repology.parsers import Parser
from repology.transformer import PackageTransformer
from typing import Iterable

def _expand_multiline_licenses(text: str) -> Iterable[str]: ...

class SolusIndexParser(Parser):
    def iter_parse(self, path: str, factory: PackageFactory, transformer: PackageTransformer) -> Iterable[PackageMaker]: ...
