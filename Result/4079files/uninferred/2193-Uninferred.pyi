from typing import Any, Optional

class vMF:
    kappa: Any = ...
    mean: Any = ...
    name: Any = ...
    def __init__(self, name: Optional[Any] = ..., mean: Optional[Any] = ..., kappa: Optional[Any] = ...) -> None: ...
    def __repr__(self): ...
    num_samples: Any = ...
    def sample(self, mean: Optional[Any] = ..., kappa: Optional[Any] = ..., num_samples: int = ..., direct_output: bool = ...): ...
    samples_xyz: Any = ...
    samples_azdip: Any = ...
    def add_orientation_data(self, orient: Any) -> None: ...
    def estimate_vMF_params(self) -> None: ...
    _verts3d: Any = ...
    def plot_samples_3D(self): ...
    def plot_stereonet(self, poles: bool = ..., samples: Optional[Any] = ...) -> None: ...
    def _generate_samples(self): ...
    def _sample_weight(self, dim: Any): ...
    def _sample_orthonormal_to(self): ...
    def _cartesian2spherical(self, xyz: Any): ...
    def cart2sph_real(self, xyz: Any): ...
    def _spherical2cartesian(self, orient: Any): ...
