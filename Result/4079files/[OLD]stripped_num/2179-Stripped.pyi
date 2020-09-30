# (generated with --quick)

from typing import Any, Dict, List, Tuple, Union

OP_CHECKSIG: bytes
OP_DUP: bytes
OP_EQUAL: bytes
OP_EQUALVERIFY: bytes
OP_HASH160: bytes
P2PKH_PREFIXES: List[str]
P2SH_PREFIXES: List[str]
all_outputs_raw: Any
app: Any
arg_inputs: List[Dict[str, Any]]
arg_outputs: List[Dict[str, Union[int, str]]]
bip32_to_address: Dict[str, Any]
bip32path: str
bitcoin: Any
dongle: Any
idx: int
input: Any
new_input: Dict[str, Any]
new_transaction: Any
o: Dict[str, Union[int, str]]
out: Any
output: Any
prev_transaction: Any
pubkey: Any
pubkey_hash: Any
pubkey_hash_from_script: Any
raw_tx: Any
sig: Any
starting: bool
transactions_cache: Dict[str, str]
trusted_input: Any
trusted_inputs: list
tx_raw: Any
utxo: Dict[str, Union[int, str]]
utxo_tx_index: int
utxos_to_spend: List[Dict[str, Union[int, str]]]

def __getattr__(name) -> Any: ...
def compose_tx_locking_script(dest_address) -> Any: ...
def extract_pkh_from_locking_script(script) -> Any: ...
def read_varint(buffer, offset) -> Tuple[Any, int]: ...
