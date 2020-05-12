# (generated with --quick)

import enum
from typing import Any, Dict, Tuple, Type, TypeVar

Enum: Type[enum.Enum]
Property: Any
VOL_NORM: Any

EnumType = TypeVar('EnumType', bound=enum.Enum)

class Channel(enum.Enum):
    BACKGROUND: str
    BODY: str
    CON_CMD: str
    DEFAULT: str
    GUNFIRE: str
    ITEMS: str
    PLAYER_VOICE: str
    STREAMING: str
    TF2_ANNOUNCER: str
    VOICE: str
    __doc__: str

class Level(enum.Enum):
    SNDLVL_100dB: str
    SNDLVL_105dB: str
    SNDLVL_110dB: str
    SNDLVL_120dB: str
    SNDLVL_125dB: str
    SNDLVL_130dB: str
    SNDLVL_140dB: str
    SNDLVL_145dB: str
    SNDLVL_150dB: str
    SNDLVL_180dB: str
    SNDLVL_20dB: str
    SNDLVL_25dB: str
    SNDLVL_30dB: str
    SNDLVL_35dB: str
    SNDLVL_40dB: str
    SNDLVL_45dB: str
    SNDLVL_50dB: str
    SNDLVL_55dB: str
    SNDLVL_65dB: str
    SNDLVL_70dB: str
    SNDLVL_80dB: str
    SNDLVL_85dB: str
    SNDLVL_90dB: str
    SNDLVL_95dB: str
    SNDLVL_GUNFIRE: str
    SNDLVL_IDLE: str
    SNDLVL_NONE: str
    SNDLVL_NORM: str
    SNDLVL_STATIC: str
    SNDLVL_TALKING: str
    __doc__: str
    def __str__(self) -> Any: ...

class Pitch(float, enum.Enum):
    PITCH_HIGH: float
    PITCH_LOW: float
    PITCH_NORM: float
    def __str__(self) -> Any: ...

class Sound:
    __doc__: str
    channel: Any
    level: Any
    name: Any
    pitch: Any
    sounds: Any
    stack_start: Any
    stack_stop: Any
    stack_update: Any
    volume: Any
    def __init__(self, name, sounds, volume, channel, level, pitch, stack_start, stack_update, stack_stop) -> None: ...
    def export(self, sounds, file) -> None: ...
    @classmethod
    def parse(cls, file) -> Dict[Any, Sound]: ...

class VOLUME(enum.Enum):
    VOL_NORM: str
    __doc__: str

def conv_float(val, default = ...) -> float: ...
def join_float(val) -> str: ...
def split_float(val, enum, default) -> Tuple[Any, Any]: ...
