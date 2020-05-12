# (generated with --quick)

import numpy
from typing import Any, TextIO, Tuple

Gamora: Any
c: Any
carmaWrap_context: Any
csr_matrix: Any
drax: Any
gpudevices: numpy.ndarray
h5py: Any
np: module
plt: Any
stdout: TextIO
time: module

def add_fitting_to_psf(filename, otf, otffit) -> Any: ...
def intersample(Cvvmap, pupilImage, IFImage, pixscale, dactu, lambdaIR) -> Any: ...
def psf_rec_Vii(filename, err = ..., fitting = ..., covmodes = ..., cov = ...) -> Tuple[Any, numpy.ndarray, Any, Any]: ...
def psf_rec_vii_cpu(filename) -> Tuple[Any, Any, Any]: ...
def test_Vii(filename) -> None: ...
