# (generated with --quick)

from typing import Any

hvac: Any

class KeyManager:
    __doc__: str
    def delete(self, *args, **kwarg) -> dict: ...
    def get(self, *args, **kwargs) -> dict: ...
    def set(self, *args, **kwargs) -> dict: ...

class VaultKeyManager(KeyManager):
    __doc__: str
    vault: Any
    def __init__(self, vault) -> None: ...
    def delete(self, *args, **kwargs) -> dict: ...
