from genericWrapper4AC.domain_specific.satwrapper import SatWrapper
from typing import Any

class MiniSATWrapper(SatWrapper):
    def get_command_line_args(self, runargs: Any, config: Any): ...
