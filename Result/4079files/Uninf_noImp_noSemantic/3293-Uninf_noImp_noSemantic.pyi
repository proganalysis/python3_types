from typing import Any

TxApiBitcoin: Any
TxApiTestnet: Any
TxApiZencash: Any
TxApiDash: Any
tests_dir: Any

def test_tx_api_gettx() -> None: ...
def test_tx_api_current_block() -> None: ...
def test_tx_api_get_block_hash() -> None: ...
def test_tx_api_dash_dip2() -> None: ...