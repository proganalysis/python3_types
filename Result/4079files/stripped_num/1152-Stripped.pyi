# (generated with --quick)

from typing import Any

nacl: module
settings: Any

def decrypt_text(key, encrypted_text) -> Any: ...
def encrypt_text(key, sensitive_text) -> Any: ...
def pepper(encrypted_report) -> Any: ...
def unpepper(peppered_report) -> Any: ...