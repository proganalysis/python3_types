# (generated with --quick)

from typing import Any, Tuple, Union

Figure: Any
FigureCanvas: Any
QEvent: Any
VMIN: int
Y_MAX: int
Y_MIN: int
matplotlib: Any
np: module
pyqtSignal: Any
wave: module

class Plot_waveform_RT(Any):
    canvas: Any
    cursor_color: str
    figure: Any
    frame_rate: Any
    interval: int
    media_length: Any
    sendEvent: Any
    sound_info: Any
    time_mem: Union[float, int]
    wav_file_path: str
    def __init__(self) -> None: ...
    def eventFilter(self, receiver, event) -> bool: ...
    def get_wav_info(self, wav_file: str) -> Tuple[Any, Any]: ...
    def load_wav(self, wav_file_path: str) -> dict: ...
    def plot_waveform(self, current_time: float) -> None: ...

def __getattr__(name) -> Any: ...
