# (generated with --quick)

from typing import Any

GaussianMixture: Any
Segment: Any
Timeline: Any
np: module
one_hot_decoding: Any
pairwise: Any
scipy: Any

class Binarize(object):
    __doc__: str
    log_scale: Any
    min_duration_off: Any
    min_duration_on: Any
    offset: Any
    onset: Any
    pad_offset: Any
    pad_onset: Any
    scale: Any
    def __init__(self, onset = ..., offset = ..., scale = ..., log_scale = ..., pad_onset = ..., pad_offset = ..., min_duration_on = ..., min_duration_off = ...) -> None: ...
    def apply(self, predictions, dimension = ...) -> Any: ...

class GMMResegmentation(object):
    __doc__: str
    n_components: Any
    n_iter: Any
    window: Any
    def __init__(self, n_components = ..., n_iter = ..., window = ...) -> None: ...
    def apply(self, annotation, features) -> Any: ...

class Peak(object):
    __doc__: str
    alpha: Any
    log_scale: Any
    min_duration: Any
    scale: Any
    def __init__(self, alpha = ..., min_duration = ..., scale = ..., log_scale = ...) -> None: ...
    def apply(self, predictions, dimension = ...) -> Any: ...
