from datetime import date
from typing import Any, Dict, Set

log: Any

def calc_kelly_leverages(securities: Set[str], start_date: date, end_date: date, risk_free_rate: float=...) -> Dict[str, float]: ...
def main() -> None: ...
