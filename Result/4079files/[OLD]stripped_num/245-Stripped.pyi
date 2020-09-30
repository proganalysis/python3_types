# (generated with --quick)

import pathlib
from typing import Any, Tuple, Type

CLVL: Any
KEY: Any
Path: Type[pathlib.Path]
PiCamera: Any
getparams: Any
grabframe: Any
np: module
setparams: Any

def _preview(cam, preview, bit8) -> Tuple[Any, Any]: ...
def _writesetup(outfn, Nimg, img) -> Any: ...
def pibayerraw(Nimg, exposure_sec, bit8 = ..., preview = ..., outfn = ...) -> None: ...
def sleep(secs: float) -> None: ...
def updatepreview(img, hi, ht) -> None: ...
def writeframe(f, i, img, cam) -> None: ...
