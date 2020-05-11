# (generated with --quick)

import itertools
from typing import Any, List, Tuple, Type

chain: Type[itertools.chain]
citizens: Any
datetime: Type[datetime.datetime]
fidelity: Any
fidelity_visa: Any
schema: Any
sys: module
venmo: Any

class BankException(Exception):
    __doc__: str

def _pick_module(bank_config) -> Any: ...
def _transform(transaction, env, columns) -> list: ...
def accounts_by_bank(configs_by_key, iolayer) -> dict: ...
def banks() -> list: ...
def fetch(key, bank_config, iolayer) -> None: ...
def list_transactions(key, config, iolayer) -> Any: ...
def map_rules(rules_function, transactions) -> Tuple[Any, List[str]]: ...
