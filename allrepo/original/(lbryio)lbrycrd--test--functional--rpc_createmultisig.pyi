# (generated with --quick)

from typing import Any

BitcoinTestFramework: Any
decimal: module

class RpcCreateMultiSigTest(Any):
    add: Any
    final: Any
    moved: Any
    nkeys: int
    nsigs: int
    num_nodes: int
    output_type: str
    priv: Any
    pub: Any
    setup_clean_chain: bool
    def checkbalances(self) -> None: ...
    def do_multisig(self) -> None: ...
    def get_keys(self) -> None: ...
    def run_test(self) -> None: ...
    def set_test_params(self) -> None: ...
    def skip_test_if_missing_module(self) -> None: ...
