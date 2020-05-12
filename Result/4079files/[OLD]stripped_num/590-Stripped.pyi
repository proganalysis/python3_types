# (generated with --quick)

from typing import Any, Optional

ParseError: Any
Point: Any
Region: Any
RunConfiguration: Any
SeedZone: Any
TransferLimit: Any
get_elevation_at_point: Any
serializers: Any

class GenerateReportSerializer(Any):
    configuration: Any
    opacity: Any
    tile_layers: Any
    zoom: Any

class RegionSerializer(Any):
    Meta: type

class RunConfigurationSerializer(Any):
    Meta: type
    configuration: Any

class SeedZoneSerializer(Any):
    Meta: type
    _elevation: Any
    _elevation_at_point: Any
    elevation_at_point: Any
    elevation_band: Any
    def get_elevation_at_point(self, obj) -> Any: ...
    def get_elevation_band(self, obj) -> Optional[list]: ...

class TransferLimitSerializer(Any):
    Meta: type
    zone: SeedZoneSerializer
