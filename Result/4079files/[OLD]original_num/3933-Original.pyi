# (generated with --quick)

import ..soundapi.miniaudio
import ..soundapi.pyaudio
import ..soundapi.soundcard
import ..soundapi.sounddevice
import ..soundapi.winsound
from typing import Any, Type

AudioApi: Any
MiniaudioMixed: Type[..soundapi.miniaudio.MiniaudioMixed]
MiniaudioSequential: Type[..soundapi.miniaudio.MiniaudioSequential]
PyAudioMixed: Type[..soundapi.pyaudio.PyAudioMixed]
PyAudioSequential: Type[..soundapi.pyaudio.PyAudioSequential]
SoundcardThreadMixed: Type[..soundapi.soundcard.SoundcardThreadMixed]
SoundcardThreadSequential: Type[..soundapi.soundcard.SoundcardThreadSequential]
SounddeviceMixed: Type[..soundapi.sounddevice.SounddeviceMixed]
SounddeviceThreadMixed: Type[..soundapi.sounddevice.SounddeviceThreadMixed]
SounddeviceThreadSequential: Type[..soundapi.sounddevice.SounddeviceThreadSequential]
WinsoundSeq: Type[..soundapi.winsound.WinsoundSeq]
available_mix_play_apis: list
available_sequential_play_apis: list

def best_api(samplerate: int = ..., samplewidth: int = ..., nchannels: int = ..., frames_per_chunk: int = ..., mixing: str = ..., queue_size: int = ...) -> Any: ...
