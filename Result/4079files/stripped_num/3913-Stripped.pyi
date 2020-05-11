# (generated with --quick)

from typing import Any, NoReturn

EYRA_ROOT: str
MySQLdb: Any
_db: Any
argparse: module
args: argparse.Namespace
csv: module
dbConst: Any
log: Any
newPath: Any
os: module
parser: argparse.ArgumentParser
sh: Any
sys: module
uuid: module

def copyToFilesystem(data_path, session_path, session_id) -> None: ...
def insertIntoDatabase(session_path, tsv_data) -> NoReturn: ...
def run(data_path, tsv_name) -> None: ...
