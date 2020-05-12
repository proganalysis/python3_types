# (generated with --quick)

from typing import Any

GdalAlgorithm: Any
GdalUtils: Any
QgsProcessingException: Any
QgsProcessingParameterBand: Any
QgsProcessingParameterBoolean: Any
QgsProcessingParameterDefinition: Any
QgsProcessingParameterNumber: Any
QgsProcessingParameterRasterDestination: Any
QgsProcessingParameterRasterLayer: Any
QgsProcessingParameterString: Any
QgsRasterFileWriter: Any
__author__: str
__copyright__: str
__date__: str
os: module
pluginPath: str

class hillshade(Any):
    ALTITUDE: str
    AZIMUTH: str
    BAND: str
    COMBINED: str
    COMPUTE_EDGES: str
    EXTRA: str
    INPUT: str
    MULTIDIRECTIONAL: str
    OPTIONS: str
    OUTPUT: str
    SCALE: str
    ZEVENBERGEN: str
    Z_FACTOR: str
    def __init__(self) -> None: ...
    def commandName(self) -> str: ...
    def displayName(self) -> Any: ...
    def getConsoleCommands(self, parameters, context, feedback, executing = ...) -> list: ...
    def group(self) -> Any: ...
    def groupId(self) -> str: ...
    def initAlgorithm(self, config = ...) -> None: ...
    def name(self) -> str: ...
