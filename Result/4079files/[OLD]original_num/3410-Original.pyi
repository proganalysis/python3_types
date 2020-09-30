# (generated with --quick)

from typing import Any

Account: Any
AccountStates: Any
AccountTypes: Any
anchore_now: Any

class AccountAlreadyExistsError(Exception):
    account_name: Any
    def __init__(self, account_name) -> None: ...

class AccountNotFoundError(Exception):
    account_name: Any
    def __init__(self, account_name) -> None: ...

class InvalidStateError(Exception):
    current_state: Any
    desired_state: Any
    def __init__(self, current_state, desired_state) -> None: ...

def add(account_name, state = ..., account_type = ..., email = ..., session = ...) -> Any: ...
def delete(name, session = ...) -> bool: ...
def get(name, session = ...) -> Any: ...
def get_all(with_state = ..., session = ...) -> list: ...
def update_state(name, new_state, session = ...) -> Any: ...
