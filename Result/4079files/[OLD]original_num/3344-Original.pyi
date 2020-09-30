# (generated with --quick)

import argparse
import json.encoder
from typing import Any, Callable, List, NoReturn, Optional, Tuple, Type, Union

ArgumentParser: Type[argparse.ArgumentParser]
Pydradis3: Any
argv: List[str]
csv: module
pyHaveIBeenPwned: Any
scriptInstance: HaveIBeenPwndDradis
version: str

class HaveIBeenPwndDradis(object):
    arg: argparse.Namespace
    dradisApiToken: Any
    dradisDebug: bool
    dradisProjectId: Any
    dradisSession: Any
    dradisUrl: Any
    querySession: Any
    verifyCert: bool
    def createEvidence(self, nodeId, projectId, issueId, evidenceData) -> Any: ...
    def createIssue(self, userEmailOrDomain, projectId, nodeId) -> Any: ...
    def createNode(self, nodeName: str, projectId: int) -> Any: ...
    def performQuery(self, userEmailOrDomain: str, projectId: str) -> None: ...
    def processArguments(self) -> argparse.Namespace: ...
    def run(self) -> None: ...
    def searchApi(self, query: str) -> Any: ...

def dumps(obj, skipkeys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., cls: Optional[Type[json.encoder.JSONEncoder]] = ..., indent: Optional[Union[int, str]] = ..., separators: Optional[Tuple[str, str]] = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ..., **kwds) -> str: ...
def exit(arg: object = ...) -> NoReturn: ...
