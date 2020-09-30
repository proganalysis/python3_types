# (generated with --quick)

from typing import Any

SignedJwtAssertionCredentials: Any
argparse: module
args: argparse.Namespace
create_daily_supps: bool
create_streaks: bool
create_timestamped_supps: bool
datetime: module
gspread: Any
json: module
l2z: Lifelogger_to_Zenobase
logging: module
parser: argparse.ArgumentParser
pprint: module
pyzenobase: Any
re: module
time: module

class Lifelogger_to_Zenobase:
    gc: Any
    ll: Any
    streaks_bucket: Any
    supplements_bucket: Any
    zapi: Any
    def __init__(self, google_oauth_json_path, zenobase_username, zenobase_password, streaks_bucket_name = ..., supplements_bucket_name = ...) -> None: ...
    def _create_events(self, bucket_id, events, debugging = ...) -> None: ...
    def close(self) -> None: ...
    def create_daily_supps(self) -> None: ...
    def create_streaks(self) -> None: ...
    def create_timestamped_supps(self) -> None: ...
    @staticmethod
    def get_dates(raw_table) -> Any: ...
    def get_main(self) -> Any: ...
    def get_raw_table(self, sheetname) -> Any: ...

def times_to_dt(d, times) -> list: ...
