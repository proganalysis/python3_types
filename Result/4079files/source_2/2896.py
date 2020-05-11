import hashlib
from typing import Iterable

from simplest.network import Network
from simplest.transaction import SignedTransaction


class Block:
    def __init__(self, trxs: Iterable[SignedTransaction], prev_block: 'Block'):
        print('[Block.init] trxs: {}, prev_block: {}'.format(trxs, prev_block))
        self.id = ''
        self.secret = 0
        self.trxs = trxs
        self.prev_block = prev_block
        while not Network.validate_block_id(self.id):
            self.secret += 1
            self.id = self.create_id(self.trxs, self.prev_block, self.secret)

    def validate(self) -> bool:
        return self.create_id(self.trxs, self.prev_block, self.secret) == self.id and Network.validate_block_id(self.id)

    @staticmethod
    def create_id(trxs: Iterable[SignedTransaction], prev_block: 'Block', secret: int) -> str:
        def to_bytes(x: object):
            return bytearray(str(x), 'UTF_8')

        initial = [] if prev_block is None else to_bytes(prev_block.id)
        initial.extend(to_bytes(secret))
        byte_trxs = [to_bytes(trx) for trx in trxs]
        byte_trxs.insert(0, initial)
        return hashlib.sha256(to_bytes(byte_trxs)).hexdigest()

    def __str__(self) -> str:
        return 'Block of {} transactions (Block Id: {}, Previous Block Id: {}, secret: {})'.format(
            len(list(self.trxs)), self.id, None if self.prev_block is None else self.prev_block.id, self.secret)
