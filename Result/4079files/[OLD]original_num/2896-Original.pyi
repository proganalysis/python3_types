# (generated with --quick)

from typing import Any, Iterable

Network: Any
SignedTransaction: Any
hashlib: module

class Block:
    id: Any
    prev_block: Block
    secret: int
    trxs: Iterable
    def __init__(self, trxs: Iterable, prev_block: Block) -> None: ...
    def __str__(self) -> str: ...
    @staticmethod
    def create_id(trxs: Iterable, prev_block: Block, secret: int) -> str: ...
    def validate(self) -> bool: ...
