from typing import Any

def encrypt_text(key: Any, sensitive_text: Any): ...
def decrypt_text(key: Any, encrypted_text: Any): ...
def pepper(encrypted_report: Any): ...
def unpepper(peppered_report: Any): ...