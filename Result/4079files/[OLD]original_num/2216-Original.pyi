# (generated with --quick)

from typing import Any, BinaryIO, Type

RawTextHelpFormatter: Type[argparse.RawTextHelpFormatter]
argparse: module
base64: module
lArgParser: argparse.ArgumentParser
lArgs: argparse.Namespace
lEncryptionActionGroup: argparse._MutuallyExclusiveGroup
lFile: BinaryIO
lInput: bytearray
lInputSourceGroup: argparse._MutuallyExclusiveGroup
lKey: int
lKeyOrBruteforceActionGroup: argparse._MutuallyExclusiveGroup
lModulus: Any
sys: module

def bruteforce_plaintext(pInput: bytearray, pModulus: int, pVerbose: bool) -> None: ...
def decrypt(pCiphertextBytes: bytearray, pKey: int, pModulus: int) -> bytearray: ...
def derive_key(pKeyString: str, pModulus: int) -> int: ...
def do_decrypt(pByte: int, pKey: int, pModulus: int) -> int: ...
def do_encrypt(pByte: int, pKey: int, pModulus: int) -> int: ...
def encrypt(pPlaintextBytes: bytearray, pKey: int, pModulus: int) -> bytearray: ...
def is_unprintable(pBytes: bytearray) -> bool: ...
def key_is_involutary(pKey: int, pModulus: int) -> bool: ...
def key_is_trivial(pKey: int, pModulus: int) -> bool: ...
def print_ciphertext(pInput: bytearray, pKey: int, pModulus: int, pVerbose: bool, pOutputFormat: str) -> None: ...
def print_plaintext(pInput: bytearray, pKey: int, pModulus: int, pVerbose: bool) -> None: ...