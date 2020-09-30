# (generated with --quick)

from typing import Any, Dict, Optional, Tuple

Sample: Any
glob: module
itertools: module
os: module
random: module
sys: module

class DrumKit:
    instruments: Dict[Any, Instrument]
    def __init__(self) -> None: ...
    def load(self, samples_location) -> None: ...

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
    _samples_location: Any
    groups: list
    name: Any
    total_sample_memory: Any
    def __init__(self, name) -> None: ...
    @classmethod
    def from_name_and_groups(cls, name, groups) -> Any: ...
    def get_group(self, velocity) -> Any: ...
    def group(self, line) -> Group: ...
    def load_sfz(self, filename, samples_location) -> None: ...
    def region(self, line) -> Optional[Region]: ...

class Region:
    hi_rand: Optional[float]
    lo_rand: Optional[float]
    sample: Any
    seq: Optional[int]
    def __init__(self) -> None: ...
