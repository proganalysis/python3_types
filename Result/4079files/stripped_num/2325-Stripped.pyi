# (generated with --quick)

import datetime
import io
from typing import Any, List, Optional, Pattern, Tuple, Type, TypeVar

STATS: Pattern[str]
Stats: Any
StringIO: Type[io.StringIO]
VERSION: Pattern[str]
create_firehose: Any
fgcc: Any
glob: module
os: module
re: module
run_command: Any
run_logged: Any
safe_run: Any
timedelta: Type[datetime.timedelta]

_T7 = TypeVar('_T7')

def checkout(dsc_url) -> Any: ...
def ensure_chroot_sanity(chroot_name) -> bool: ...
def get_version() -> Tuple[str, str]: ...
def parse_sbuild_log(log, sut) -> Any: ...
def run(jlog, job, jdata) -> Tuple[bool, List[str], Optional[str]]: ...
def sbuild(jlog, dsc, maintainer, suite, affinity, build_arch, build_indep, analysis: _T7) -> Tuple[_T7, Any, Any, List[str]]: ...
