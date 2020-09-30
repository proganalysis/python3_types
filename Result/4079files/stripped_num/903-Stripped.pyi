# (generated with --quick)

import rpc
from typing import Any, Dict, Type, Union

RPC: Type[rpc.RPC]
binascii: module
config: module
ecdsa: Any
json: module
my_rpc: rpc.RPC
random: module
requests: module
system_random: random.SystemRandom

class Wallet:
    labels: Dict[Union[bytes, str], Any]
    public_key: Dict[Union[bytes, str], str]
    def __init__(self) -> None: ...
    def balance(self) -> Any: ...
    def generate_address(self, label) -> str: ...
    def send(self, to, amount) -> None: ...
    def transactions(self) -> list: ...

def key_to_string(key) -> str: ...
