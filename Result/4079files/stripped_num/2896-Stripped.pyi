# (generated with --quick)

from typing import Any

Network: Any
SignedTransaction: Any
hashlib: module

class Block:
    id: str
    prev_block: Any
    secret: int
    trxs: Any
    def __init__(self, trxs, prev_block) -> None: ...
    def __str__(self) -> str: ...
    @staticmethod
    def create_id(trxs, prev_block, secret) -> str: ...
    def validate(self) -> Any: ...
