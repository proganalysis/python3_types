# (generated with --quick)

from typing import Any, Dict

MAX_RATIO_STANDARD_DEVIATION: int
MIN_NUMBER_OF_MASTER_BUILDS: int
current_build: Any
current_master_ratio: Any
json: module
logging: module
master_branch: Dict[str, Any]
python2_build_number: str
python3_build_number: str
requests: module
sys: module

def get_current_build_performance(python2_build_number, python3_build_number) -> Any: ...
def get_master_branch_performance() -> Dict[str, Any]: ...
