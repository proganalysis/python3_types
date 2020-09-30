# (generated with --quick)

from typing import Any, Optional

QtCore: Any
QtGui: Any
QtWidgets: Any
Serial: Any
SerialException: Any
TemplateBaseClass: Any
WindowTemplate: Any
list_ports: Any
np: module
pg: Any
struct: module
sys: module
threading: module
time: module
win: MainWindow

class Emitter(Any):
    newSample: Any
    def __init__(self) -> None: ...
    def connect(self) -> None: ...
    def emit(self, data) -> None: ...

class Generator(Any):
    newData: Any
    def __init__(self, f) -> None: ...
    def run(self) -> Any: ...

class MainWindow(Any):
    data: list
    plots: list
    portSelector: PortSelector
    ui: Any
    def __init__(self) -> None: ...
    def closeEvent(self, event) -> None: ...
    def update(self, sample) -> None: ...

class Port(Any):
    close_request: None
    description: Any
    emitter: Optional[Emitter]
    port: Any
    readThread: Optional[threading.Thread]
    serial: Any
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, port_data, *args, **kwargs) -> None: ...
    def __repr__(self) -> Any: ...
    def close(self) -> None: ...
    def isOpen(self) -> Any: ...
    def listen(self) -> None: ...
    def open(self, baudrate, parity, bytesize) -> None: ...

class PortSelector:
    baudrate_combo: Any
    baudrate_validator: Any
    bytesize_combo: Any
    check_availability_list: list
    check_availability_timer: Any
    list_w: Any
    parity_combo: Any
    port: None
    refresh_timer: Any
    def __init__(self, list_w, baudrate_combo, parity_combo, bytesize_combo) -> None: ...
    def check_availability(self) -> None: ...
    def getPortList(self) -> list: ...
    def refresh(self) -> None: ...
    def setPort(self, port) -> None: ...
