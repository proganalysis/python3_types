# (generated with --quick)

from typing import List

os: module
winsound: module

class SoundPlayer:
    NOTES: List[str]
    jab_wave_exists: bool
    launch_wav_exists: bool
    def noteFreq(name: SoundPlayer, oct) -> int: ...
    def play_no_jab_punish() -> None: ...
    def play_no_launch_punish() -> None: ...
