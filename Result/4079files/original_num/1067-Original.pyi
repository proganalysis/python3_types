# (generated with --quick)

from typing import Any, Dict

WrfRunnerException: Any
f90nml: Any
glob: module
log: logging.Logger
logging: module
os: module
subprocess: module

def check_wrf_output() -> bool: ...
def create_namelist_patch(initialization_time, length_hours = ...) -> Dict[str, Dict[str, Any]]: ...
def link_metgrid_outputs(src, dst) -> None: ...
def run_real() -> None: ...
def run_wrf(cores) -> None: ...
