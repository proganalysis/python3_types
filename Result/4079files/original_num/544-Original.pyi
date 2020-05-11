# (generated with --quick)

from typing import Any, Dict

Simu: Any
warnings: module

class SimuPointProcess(Any):
    __doc__: str
    _attrinfos: Dict[str, Dict[str, bool]]
    _end_time: None
    _pp: None
    end_time: Any
    intensity_track_step: Any
    intensity_tracked_times: Any
    max_jumps: Any
    n_nodes: Any
    n_total_jumps: Any
    seed: Any
    simulation_time: Any
    timestamps: Any
    tracked_intensity: Any
    def __init__(self, end_time = ..., max_jumps = ..., seed = ..., verbose = ...) -> None: ...
    def _simulate(self) -> None: ...
    def is_intensity_tracked(self) -> Any: ...
    def reset(self) -> None: ...
    def set_timestamps(self, timestamps, end_time = ...) -> None: ...
    def threshold_negative_intensity(self, allow = ...) -> None: ...
    def track_intensity(self, intensity_track_step = ...) -> None: ...
