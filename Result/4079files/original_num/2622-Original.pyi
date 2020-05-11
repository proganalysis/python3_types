# (generated with --quick)

from typing import Any, Dict, List

__author__: str
__copyright__: str
__credits__: List[str]
__license__: str
__maintainer__: str
__status__: str
__version__: str
os: module
re: module
struct: module

class AssembledParsedFile:
    __doc__: str
    assemblySize: Any
    externalReferences: Any
    internalReferences: Any
    name: Any
    text: Any
    def __init__(self, inputFile = ..., skipValidationAndLogic = ...) -> None: ...
    def _buildDictFromInnerReferenceData(self, data = ...) -> Dict[nothing, nothing]: ...
    def _extractAssemblySize(self, data = ...) -> Any: ...
    def _extractGlobalReferences(self, data = ...) -> Dict[nothing, nothing]: ...
    def _extractInternalReferences(self, data = ...) -> Dict[nothing, nothing]: ...
    def _extractText(self, data = ...) -> bytes: ...
    def _parseInputFile(self, inputFile = ...) -> None: ...
