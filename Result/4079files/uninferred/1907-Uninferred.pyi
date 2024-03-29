from antlr4 import *
from .Antlr_Files.ClingoListener import ClingoListener
from .Antlr_Files.ClingoParser import ClingoParser
from typing import Any

def rearrangePWSandRLS(relations: Any, pws: Any): ...
def loadIntoPandas(relations: Any, pws: Any, dfs: Any) -> None: ...

class AntlrClingoListener(ClingoListener):
    pws: Any = ...
    relations: Any = ...
    expected_pws: int = ...
    curr_pw: Any = ...
    curr_pw_id: int = ...
    curr_fact: Any = ...
    curr_fact_data: Any = ...
    curr_fact_depth: int = ...
    n_facts: int = ...
    dfs: Any = ...
    silent: bool = ...
    def __init__(self) -> None: ...
    def enterClingoOutput(self, ctx: Any) -> None: ...
    def enterPw(self, ctx: Any) -> None: ...
    def enterFact(self, ctx: Any) -> None: ...
    def enterFact_text(self, ctx: ClingoParser.Fact_textContext) -> Any: ...
    def exitFact(self, ctx: Any) -> None: ...
    def exitPw(self, ctx: Any) -> None: ...
    def enterOptimum(self, ctx: Any) -> None: ...
    def enterOptimization(self, ctx: Any) -> None: ...
    def enterModels(self, ctx: Any) -> None: ...
    def exitClingoOutput(self, ctx: Any) -> None: ...

def __parse_clingo_output__(input_stream: Any, silent: bool = ..., print_parse_tree: bool = ...): ...
def parse_clingo_output_from_file(fname: Any, silent: bool = ..., print_parse_tree: bool = ...): ...
def parse_clingo_output_from_string(clingo_output_string: Any, silent: bool = ..., print_parse_tree: bool = ...): ...
