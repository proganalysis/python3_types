# (generated with --quick)

import datetime
from typing import Any, Tuple, Type

MasterPassword: Any
PrivateKey: Any
Wallet: Any
configStorage: Any
dt: Type[datetime.datetime]
env_unlocked: Any
parse_time: Any

def generate_signing_key() -> Tuple[Any, Any]: ...
def head_block_lag(steemd_instance) -> int: ...
def unlock_steempy_wallet() -> None: ...
def wait_for_healthy_node(steem, seconds = ...) -> None: ...
