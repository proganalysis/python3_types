# (generated with --quick)

from typing import Any, Dict, List, Optional, Tuple

Sample: Any
glob: module
itertools: module
os: module
random: module
sys: module

class DrumKit:
    instruments: Dict[str, Instrument]
    def __init__(self) -> None: ...
    def load(self, samples_location: str) -> None: ...

class Group:
    _seq: int
    _uses_random: bool
    amp_veltrack: int
    ampeg_release: float
    group: int
    hi_vel: int
    key: int
    lo_vel: int
    regions: list
    seq_length: int
    volume: float
    def __init__(self) -> None: ...
    def get_sample(self) -> Tuple[float, Any]: ...
    def initialize(self) -> None: ...

class Instrument:
    _samples_location: str
    groups: list
    name: str
    total_sample_memory: Any
    def __init__(self, name: str) -> None: ...
    @classmethod
    def from_name_and_groups(cls, name: str, groups: List[Group]) -> Instrument: ...
    def get_group(self, velocity: int) -> Group: ...
    def group(self, line: str) -> Group: ...
    def load_sfz(self, filename: str, samples_location: str) -> None: ...
    def region(self, line: str) -> Optional[Region]: ...

class Region:
    hi_rand: Optional[float]
    lo_rand: Optional[float]
    sample: Any
    seq: Optional[int]
    def __init__(self) -> None: ...
