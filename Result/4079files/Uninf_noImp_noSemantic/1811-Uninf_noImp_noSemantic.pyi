import pandas as pd
from solcast_frames.latlng import LatLng
from typing import Any

class PowerFrameHandler:
    def forecast(lat_lng: LatLng, capacity: int, **kwargs: Any) -> pd.DataFrame: ...
    def estimated_actuals(lat_Lng: LatLng, capacity: int, **kwargs: Any) -> pd.DataFrame: ...
