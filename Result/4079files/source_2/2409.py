import itertools
from typing import Iterator, Sequence

import bcrypt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend


_PRINTABLE = bytes(range(33, 127)).decode('ascii')
_EMPTY_BLOCK = b'\0' * 64


def get_mask(n: int) -> int:
	return (1 << n.bit_length()) - 1


def get_stream(key: bytes, nonce: bytes) -> Iterator[int]:
	algorithm = algorithms.ChaCha20(key, nonce + b'\0' * 8)
	cipher = Cipher(algorithm, mode=None, backend=default_backend())
	encryptor = cipher.encryptor()

	while True:
		yield from encryptor.update(_EMPTY_BLOCK)


def get_password(kdf_rounds: int, character_set: Sequence[str], length: int, increment: int, site_name: str, master_password: str) -> str:
	set_size = len(character_set)
	mask = get_mask(set_size)
	nonce = increment.to_bytes(8, 'little')

	key = bcrypt.kdf(master_password.encode('utf-8'), site_name.encode('utf-8'), 32, kdf_rounds)

	byte_stream = get_stream(key, nonce)
	character_stream = (character_set[b & mask] for b in byte_stream if b & mask < set_size)

	return ''.join(itertools.islice(character_stream, length))


if __name__ == '__main__':
	print(get_password(kdf_rounds=200, character_set=_PRINTABLE, length=20, increment=0, site_name='test', master_password='test'))
