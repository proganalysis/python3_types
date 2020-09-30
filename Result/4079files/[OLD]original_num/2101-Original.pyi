# (generated with --quick)

from typing import Any, Dict

common_bandnames: Any
ee: Any
ee_bandnames: Any
iLUT: Any
os: module
pd: Any
request_meanRadiance: Any
surface_reflectance_timeseries: Any

def extractAllTimeSeries(target, geom, startDate, stopDate, missions, removeClouds = ...) -> Dict[str, Any]: ...
def loadFromExcel(target) -> Any: ...
def saveToExcel(target, allTimeSeries) -> None: ...
def timeSeries(target, geom, startDate, stopDate, missions, removeClouds = ...) -> Any: ...
def timeseries_extrator(geom, startDate, stopDate, mission, removeClouds = ...) -> Any: ...
