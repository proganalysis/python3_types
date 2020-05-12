# (generated with --quick)

from typing import Any
import unittest.case

binascii: module
extract_decrypt_kms: module
nt: Any
os: module
sys: module
unittest: module

class Test(unittest.case.TestCase):
    kms: None
    @classmethod
    def random_word(cls, length) -> str: ...
    @classmethod
    def setupAll(cls) -> None: ...
    @classmethod
    def teardownAll(cls) -> None: ...
    @classmethod
    def test_aws_decrypt(cls, to_encrypt = ...) -> None: ...
    @classmethod
    def test_aws_decrypt_with_method_file_key_parameter(cls, to_encrypt = ...) -> None: ...
    @classmethod
    def test_aws_kms_client(cls) -> None: ...
    @classmethod
    def test_several_aws_decrypt(cls, s = ..., t = ...) -> None: ...
