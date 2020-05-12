# (generated with --quick)

from typing import Any, Dict, Type

BackupRoot: Any
Interval: Any
IntervalDuration: Any
Job: Any
KeepAmount: Any
Settings: Any
backup: Any
clean_path: Any
const: Any
datetime: Type[datetime.datetime]
load_yaml: Any
log: Any
os: module
snapshot: Any
sys: module
time: module
validate: Any

def _duty_check_routine(job) -> bool: ...
def _get_due_snapshots(timestamps: Dict[Any, str], snapshots: dict, intervals: dict) -> list: ...
def _init_job(job_cfg: dict, settings, init_time: float) -> Any: ...
def _initial_job_validation_routine(job_cfg: dict) -> bool: ...
def _is_snap_due(interval, intervals: Dict[Any, int], timestamp: str) -> bool: ...
def _load_timestamps(backup_root, intervals: dict) -> Dict[Any, str]: ...
def run(job_cfg: dict, settings) -> None: ...
