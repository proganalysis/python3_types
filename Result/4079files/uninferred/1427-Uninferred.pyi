from ctypes import *
import wave
from typing import Any

declib: Any
HEADER_LEN: int

def chunks(l: Any, n: Any) -> None: ...
def decode_audio(file: Any, wav: wave.Wave_write) -> Any: ...
