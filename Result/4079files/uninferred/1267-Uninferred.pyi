from typing import Any

python2_build_number: Any
python3_build_number: Any
MAX_RATIO_STANDARD_DEVIATION: int
MIN_NUMBER_OF_MASTER_BUILDS: int

def get_master_branch_performance(): ...
def get_current_build_performance(python2_build_number: Any, python3_build_number: Any): ...

master_branch: Any
current_build: Any
current_master_ratio: Any
