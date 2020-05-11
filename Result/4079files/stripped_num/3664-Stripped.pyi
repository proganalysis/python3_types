# (generated with --quick)

from typing import NoReturn

code: module
mine: PythonShell
sys: module

class PythonShell(code.InteractiveInterpreter):
    __doc__: str
    def runall(self) -> None: ...
    def showsyntaxerror(self, filename) -> NoReturn: ...
    def showtraceback(self) -> NoReturn: ...
