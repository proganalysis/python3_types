# (generated with --quick)

import sqlite3.dbapi2
from typing import Any, Optional, Tuple

logging: module
os: module
project_functions: Any
sqlite3: module
time: module

def __getattr__(name) -> Any: ...
def load_aggregated_events_in_db(pj, selectedSubjects, selectedObservations, selectedBehaviors) -> Tuple[bool, str, Optional[sqlite3.dbapi2.Connection]]: ...
def load_events_in_db(pj, selectedSubjects, selectedObservations, selectedBehaviors, time_interval = ...) -> sqlite3.dbapi2.Cursor: ...
