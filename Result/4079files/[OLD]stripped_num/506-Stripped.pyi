# (generated with --quick)

import __future__
from typing import List, TextIO, Tuple, Type

SOURCES: int
args: List[str]
compile_begin: float
compile_end: float
compiler: Tuple[str, str]
compilers: List[Tuple[str, str]]
e: subprocess.CalledProcessError
exename: str
instance: ErrorHandlingSystem
m: Tuple[str, Type[ErrorHandlingSystem]]
matrix: List[Tuple[str, Type[ErrorHandlingSystem]]]
n: int
os: module
print_function: __future__._Feature
result: bytes
resultsh: TextIO
shlex: module
subprocess: module
sys: module
time: module

class ErrorHandlingSystem(object):
    __doc__: str
    def function_cont(self, name) -> str: ...
    def function_final(self) -> str: ...
    def generate_sources(self, no) -> None: ...
    def preamble(self, idx) -> str: ...

class ExceptionThrow(ErrorHandlingSystem): ...

class ResultErrorError(ResultErrorValue): ...

class ResultErrorValue(ErrorHandlingSystem): ...

class ResultExceptionError(ResultExceptionValue): ...

class ResultExceptionValue(ResultErrorValue): ...

class ResultExperimentalError(ResultExperimentalValue): ...

class ResultExperimentalValue(ErrorHandlingSystem): ...
