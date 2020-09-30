from UliEngineering.Units import Unit as Unit
from collections import namedtuple
from typing import Any

PTCoefficientStandard = namedtuple('PTCoefficientStandard', ['a', 'b', 'c'])
ptxIPTS68: Any
ptxITS90: Any
noCorrection: Any
pt1000Correction: Any
pt100Correction: Any

def ptx_resistance(r0: Any, t: Any, standard: Any=...) -> None: ...
def ptx_temperature(r0: Any, r: Any, standard: Any=..., poly: Any=...) -> None: ...
def checkCorrectionPolynomialQuality(r0: Any, reftemp: Any, poly: Any): ...
def computeCorrectionPolynomial(r0: Any, order: int = ...): ...

pt100_resistance: Any
pt1000_resistance: Any
pt100_temperature: Any
pt1000_temperature: Any
