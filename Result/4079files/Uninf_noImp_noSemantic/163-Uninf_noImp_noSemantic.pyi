import pandas as pd
from solcast_frames.latlng import LatLng
from typing import Any

class RadiationFrameHandler:
    def forecast(lat_lng: LatLng, **kwargs: Any) -> pd.DataFrame: ...
    def estimated_actuals(lat_lng: LatLng, **kwargs: Any) -> pd.DataFrame: ...
