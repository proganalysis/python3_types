# (generated with --quick)

from typing import Any, Tuple, Type

AltAz: Any
Angle: Any
EarthLocation: Any
ICRS: Any
SkyCoord: Any
Time: Any
datetime: Type[datetime.datetime]
np: module
str2dt: Any
u: Any
vazel2radec: Any
vradec2azel: Any

def azel2radec(az_deg: float, el_deg: float, lat_deg: float, lon_deg: float, time: datetime.datetime, usevallado: bool = ...) -> Tuple[float, float]: ...
def radec2azel(ra_deg: float, dec_deg: float, lat_deg: float, lon_deg: float, time: datetime.datetime, usevallado: bool = ...) -> Tuple[float, float]: ...
