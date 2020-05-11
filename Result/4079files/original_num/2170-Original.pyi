# (generated with --quick)

from typing import Any, TypeVar

AHRSProtocol: Any
I2CSimBase: Any
IMURegisters: Any
SPISimBase: Any
crc7: Any
hal_data: Any
wpilib: Any

_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')

class NavXI2CSim(NavXSimBase, Any):
    angle_key: str
    cap_flags: Any
    timer: Any
    def initializeI2C(self, port, status) -> None: ...
    def readI2C(self, port, deviceAddress, buffer, count: _T3) -> _T3: ...
    def writeI2C(self, port, deviceAddress, dataToSend, sendSize: _T3) -> _T3: ...

class NavXSPISim(NavXSimBase, Any):
    angle_key: str
    cap_flags: Any
    timer: Any
    def initializeSPI(self, port, status) -> None: ...
    def transactionSPI(self, port, dataToSend, dataReceived, size: _T3) -> _T3: ...
    def writeSPI(self, port, dataToSend, sendSize: _T2) -> _T2: ...

class NavXSimBase:
    __doc__: str
    cap_flags: Any
    timer: Any
    def __init__(self) -> None: ...
    def _read(self, data, count) -> None: ...
    def _write(self, data) -> None: ...
