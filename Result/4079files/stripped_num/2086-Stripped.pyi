# (generated with --quick)

from typing import Any, Optional, Tuple

CONTROL_PORT: Any
PCB_VERSION: int
T_CLOCK: Any
T_DIN: Any
T_DOUT: Any
T_GETX: Any
T_GETY: Any
T_GETZ1: Any
T_GETZ2: Any
T_IRQ: Any
X_LOW: Any
Y_HIGH: Any
asyncio: Any
pyb: Any
stm: Any

class TOUCH:
    DEFAULT_CAL: Tuple[int, float, int, float, int, float, int, float]
    asynchronous: bool
    buf_length: Any
    buff: Any
    calibration: Any
    delay: Any
    margin: Any
    pin_clock: Any
    pin_d_in: Any
    pin_d_out: Any
    pin_irq: Any
    ready: bool
    touch_talk: Any
    touched: bool
    x: int
    y: int
    def __init__(self, controller = ..., asyn = ..., *, confidence = ..., margin = ..., delay = ..., calibration = ...) -> None: ...
    def _main_thread(self) -> coroutine: ...
    def do_normalize(self, touch) -> Tuple[int, int]: ...
    def get_touch(self, initial = ..., wait = ..., raw = ..., timeout = ...) -> Optional[Tuple[Any, Any]]: ...
    def get_touch_async(self) -> None: ...
    def raw_touch(self) -> Optional[Tuple[Any, Any]]: ...
    def touch_parameter(self, confidence = ..., margin = ..., delay = ..., calibration = ...) -> None: ...
