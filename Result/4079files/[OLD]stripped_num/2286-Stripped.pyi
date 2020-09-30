# (generated with --quick)

from typing import Any, Dict, Tuple

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
    time_mem: Any
    wav_file_path: Any
    def __init__(self) -> None: ...
    def eventFilter(self, receiver, event) -> bool: ...
    def get_wav_info(self, wav_file) -> Tuple[Any, Any]: ...
    def load_wav(self, wav_file_path) -> Dict[str, Any]: ...
    def plot_waveform(self, current_time) -> None: ...

def __getattr__(name) -> Any: ...
