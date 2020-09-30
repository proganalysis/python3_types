# (generated with --quick)

from typing import Any, Dict, Set, Type

DataFrame: Any
date: Type[datetime.date]
datetime: Type[datetime.datetime]
docopt: Any
get_historical_data: Any
inv: Any
log: logging.Logger
logging: module
sys: module

def calc_kelly_leverages(securities: Set[str], start_date: datetime.date, end_date: datetime.date, risk_free_rate: float = ...) -> Dict[str, float]: ...
def main() -> None: ...
