# (generated with --quick)

from typing import Any, Type

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
def _get_due_snapshots(timestamps, snapshots, intervals) -> list: ...
def _init_job(job_cfg, settings, init_time) -> Any: ...
def _initial_job_validation_routine(job_cfg) -> bool: ...
def _is_snap_due(interval, intervals, timestamp) -> bool: ...
def _load_timestamps(backup_root, intervals) -> Any: ...
def run(job_cfg, settings) -> None: ...
