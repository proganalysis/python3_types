from btchip.btchip import *
from btchip.btchipUtils import *
from typing import Any

utxos_to_spend: Any
transactions_cache: Any
arg_outputs: Any
OP_DUP: bytes
OP_HASH160: bytes
OP_EQUALVERIFY: bytes
OP_CHECKSIG: bytes
OP_EQUAL: bytes
P2PKH_PREFIXES: Any
P2SH_PREFIXES: Any

def compose_tx_locking_script(dest_address: Any): ...
def read_varint(buffer: Any, offset: Any): ...
def extract_pkh_from_locking_script(script: Any): ...

dongle: Any
app: Any
trusted_inputs: Any
arg_inputs: Any
bip32_to_address: Any
starting: bool
raw_tx: Any
prev_transaction: Any
utxo_tx_index: Any
trusted_input: Any
bip32path: Any
pubkey: Any
pubkey_hash: Any
pubkey_hash_from_script: Any
new_transaction: Any
output: Any
all_outputs_raw: Any
out: Any
sig: Any
input: Any
tx_raw: Any
