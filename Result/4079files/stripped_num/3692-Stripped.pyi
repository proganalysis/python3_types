# (generated with --quick)

import subprocess
from typing import Any, Dict, Type

AbstractWrapper: Any
PIPE: int
Popen: Type[subprocess.Popen]
imp: module
logging: module
os: module
re: module
sys: module
wrapper: Any

class SatWrapper(Any):
    __doc__: str
    _instance: str
    inst_specific: None
    def __init__(self) -> None: ...
    def _verify_SAT(self, model, solver_output) -> bool: ...
    def _verify_via_solubility_file(self, sol) -> bool: ...
    def process_results(self, filepointer, exit_code) -> Dict[str, str]: ...
