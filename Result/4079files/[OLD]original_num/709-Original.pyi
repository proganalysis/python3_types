# (generated with --quick)

import nfc_scanner
from typing import Any, Type

Clock: Any
Logger: Any
NFCBase: Type[nfc_scanner.NFCBase]

class ScannerDummy(nfc_scanner.NFCBase):
    __doc__: str
    _initialised: bool
    name: str
    def nfc_init(self) -> bool: ...
    def on_new_intent(self, dt) -> None: ...
