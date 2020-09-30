# (generated with --quick)

from typing import Any, Dict, List

base64VlqConverter: Base64VlqConverter
collections: module
iSourceColumn: int
iSourceIndex: int
iSourceLine: int
iTargetColumn: int
iTargetLine: int
json: module
lineNrLength: int
mapVersion: int
math: module
maxNrOfSourceLinesPerModule: int
os: module
shutil: module
utils: Any

class Base64VlqConverter:
    decoding: Dict[str, int]
    encoding: str
    prefab: list
    prefabSize: int
    def __init__(self) -> None: ...
    def decode(self, segment) -> List[int]: ...
    def encode(self, numbers, init = ...) -> str: ...

class SourceMapper:
    cascadeMapdumpFile: Any
    dump: Any
    miniMappings: Any
    minify: Any
    moduleName: Any
    prettyMappings: List[list]
    shrinkMappings: List[list]
    targetDir: Any
    def __init__(self, moduleName, targetDir, minify, dump) -> None: ...
    def cascadeAndSaveMiniMap(self) -> None: ...
    def dumpDeltaMap(self, deltaMappings, infix) -> None: ...
    def dumpMap(self, mappings, infix, sourceExtension) -> None: ...
    def generateAndSavePrettyMap(self, sourceLineNrs) -> None: ...
    def generateMultilevelMap(self) -> None: ...
    def loadShrinkMap(self) -> None: ...
    def save(self, mappings, infix) -> None: ...
