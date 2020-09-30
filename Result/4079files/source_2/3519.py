# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from future.builtins import bytes, int
from io import BytesIO
import codecs
import logging
import merkle
from iscclib.base import Component
from iscclib import chunker


log = logging.getLogger(__name__)


class InstanceID(Component):
    """
    The InstanceID is made of the first 8 bytes of a merkle-root calculated
    from the cdc-chunked data to be identified. This component on its own is
    not expected to be collision resistant with its 64-bits of data. It can
    still serve as a strong discriminator in conjunction with the other
    components.

    This class also carries the cryptographically secure full sha256
    merkle-root that can be used to prove data chunks belong to a given
    Instance ID.
    """

    #: Min `code` value at default 64 bits
    CODE_MIN = u'H'
    #: Max `code` value at default 64 bits
    CODE_MAX = u'PPUYUNKI4DIAK'

    def __init__(self, *args, **kwargs):
        self.merkle_tree = kwargs.pop('merkle_tree')
        super(InstanceID, self).__init__(*args, **kwargs)

    @classmethod
    def from_data(cls, data, chunk_size=4096, bits=64):
        """
        Create InstanceID from raw binary data or stream.

        :param bytes or BytesIO data: A readable stream of bytes
        :param int chunk_size: Target size for chunks in bytes
        :param int bits: Number of bits for InstanceID
        :return InstanceID: Calculated InstanceID
        """
        if not isinstance(data, (bytes, BytesIO)):
            raise ValueError(u'data must be bytes or BytesIO')

        if not bits % 8 == 0:
            raise ValueError(u'bits must be devisible by 8')

        if not hasattr(data, 'read'):
            data = BytesIO(data)

        cgen = chunker.iter_chunks(data, normal_size_big=chunk_size, normal_size_small=40)
        leaves = [merkle.hash_function(chunk).digest() for chunk in cgen]

        return cls.from_leaves(
            leaves, prehashed=True, raw_digests=True, bits=bits
        )

    @classmethod
    def from_leaves(cls, leaves=None, prehashed=False, raw_digests=False, bits=64):
        """
        Create an InstanceID from hashes of data chunks.

        :param list leaves: List of leaves (chunks or hashes of chunks)
        :param bool prehashed: Are the leaves already hashed?
        :param bool raw_digests: Are the leaves raw_digests or hex hashes?
        :param int bits: Tartget Bit-length of InstanceID
        :return InstanceID:
        """
        assert bits % 8 == 0, u'bits must be devisible by 8'
        merkle_tree = merkle.MerkleTree(leaves, prehashed, raw_digests)
        merkle_tree.build()
        hex_hash = codecs.encode(merkle_tree.root.val, 'hex_codec')
        ident = int(hex_hash[:bits // 8 * 2], 16)
        return cls(ident, merkle_tree=merkle_tree, bits=bits)

    def get_chain(self, index):
        return self.merkle_tree.get_hex_chain(index)

    @staticmethod
    def check_chain(chain):
        return bool(merkle.check_hex_chain(chain))

    @property
    def root(self):
        """Merkle root hash (hex encoded)"""
        return codecs.encode(self.merkle_tree.root.val, 'hex_codec')

    def leaf_count(self):
        return len(self.merkle_tree.leaves)


if __name__ == '__main__':
    # Run this module for experimentation and demonstration puproses
    import time
    import bitmath as bm
    from pprint import pprint
    from iscclib.utils import sample_bytes

    b = sample_bytes(1000000, seed=6)
    iid = InstanceID.from_data(b, bits=64)
    proof_chain = iid.get_chain(0)
    pprint(proof_chain)
    print(InstanceID.check_chain(proof_chain))

    SIZES = (bm.Byte(100), bm.KiB(1), bm.KiB(100), bm.MB(1), bm.MB(10))
    ids = set()
    start_time = time.time()
    for x in SIZES:

        instance_id = InstanceID.from_data(sample_bytes(x.bytes))

        print(
            'Size:', x, 'Chunks:', instance_id.leaf_count(), 'Code:',
            instance_id, '-', repr(instance_id)
        )

        if instance_id.code in ids:
            raise ValueError('Collision found %s' % instance_id)
        else:
            ids.add(instance_id.code)

        print('Proof chain:',)

        proof = instance_id.get_chain(0)
        valid = instance_id.check_chain(proof)
        pprint(proof)

        print('Merkle Root: ', instance_id.root)
        print('Is Valid   : ', valid)
        print('##############################################################')
    print("--- %s seconds ---" % (time.time() - start_time))
