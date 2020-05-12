# (generated with --quick)

from typing import Any, Dict, List

ARGS: Dict[str, str]
CorpusImporter: Any
__author__: List[str]
__license__: str
logger: Any
os: module
subprocess: module

class TLGU(object):
    __doc__: str
    testing: Any
    def __init__(self, testing = ...) -> None: ...
    @staticmethod
    def _check_import_source() -> None: ...
    def _check_install(self) -> None: ...
    def convert(self, input_path = ..., output_path = ..., markup = ..., break_lines = ..., divide_works = ..., latin = ..., extra_args = ...) -> None: ...
    def convert_corpus(self, corpus, markup = ..., break_lines = ..., divide_works = ..., latin = ..., extra_args = ...) -> None: ...
    def divide_works(self, corpus) -> None: ...
