# (generated with --quick)

import numpy
import pathlib
from typing import Any, Optional, Tuple, Type

CLVL: Any
KEY: Any
Path: Type[pathlib.Path]
PiCamera: Any
getparams: Any
grabframe: Any
np: module
setparams: Any

def _preview(cam, preview, bit8: bool) -> Tuple[Any, Any]: ...
def _writesetup(outfn: pathlib.Path, Nimg: int, img: numpy.ndarray) -> Any: ...
def pibayerraw(Nimg: int, exposure_sec: float, bit8: bool = ..., preview = ..., outfn: Optional[pathlib.Path] = ...) -> None: ...
def sleep(secs: float) -> None: ...
def updatepreview(img, hi, ht) -> None: ...
def writeframe(f, i: int, img: numpy.ndarray, cam) -> None: ...
