# (generated with --quick)

from typing import Any, List, Tuple, TypeVar

datetime: module
filecmp: module
glob: module
inviwoapp: Any
itertools: module
json: module
logging: module
os: module
shutil: module
test: Any

_T1 = TypeVar('_T1')

class App:
    Summary: type
    app: Any
    db: Any
    git: Any
    htmlFile: Any
    jsonFile: Any
    output: Any
    reports: Any
    sqlFile: Any
    summary: Any
    testSettings: Any
    tests: List[nothing]
    def __init__(self, appPath, moduleTestPaths, outputDir, jsonFile = ..., htmlFile = ..., sqlFile = ..., runSettings = ..., testSettings = ...) -> None: ...
    def compareImages(self, test, report: _T1) -> _T1: ...
    def filterTests(self, testrange, testfilter, onlyRunFailed = ...) -> Tuple[list, list]: ...
    def linkImages(self, oldimg, newimg) -> None: ...
    def loadJson(self) -> None: ...
    def printSummary(self, out = ...) -> None: ...
    def printTestList(self, testrange = ..., testfilter = ..., printfun = ...) -> None: ...
    def runTest(self, test, run) -> Any: ...
    def runTests(self, testrange = ..., testfilter = ..., onlyRunFailed = ...) -> None: ...
    def saveHtml(self, header = ..., footer = ...) -> None: ...
    def saveJson(self) -> None: ...
    def success(self) -> bool: ...
    def updateDatabase(self, report, run) -> None: ...

def __getattr__(name) -> Any: ...
def findModuleTest(path) -> list: ...
