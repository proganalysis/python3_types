# (generated with --quick)

from typing import Any, TypeVar

BaseEstimator: Any
check_random_state: Any
clean_mask: Any
extract_patches: Any
fill: Any
np: module

_TLazyCleanPatchExtractor = TypeVar('_TLazyCleanPatchExtractor', bound=LazyCleanPatchExtractor)

class LazyCleanPatchExtractor(Any):
    indices_3d: Any
    max_patches: Any
    n_patches_: Any
    patch_shape_: Any
    patch_size: Any
    patches_: Any
    random_state: Any
    def __init__(self, patch_size = ..., random_state = ..., max_patches = ...) -> None: ...
    def fit(self: _TLazyCleanPatchExtractor, X, y = ...) -> _TLazyCleanPatchExtractor: ...
    def partial_transform(self, X = ..., batch = ...) -> Any: ...
    def shuffle(self, permutation = ...) -> None: ...
    def transform(self, X = ...) -> Any: ...
