# (generated with --quick)

from typing import Any

class Purchase:
    baths: Any
    beds: Any
    city: Any
    latitude: Any
    longitude: Any
    price: Any
    sale_date: Any
    sq__ft: Any
    state: Any
    type: Any
    zip: Any
    def __init__(self, city, zipcode, state, beds, baths, sq__ft, home_type, sale_date, price, latitude, longitude) -> None: ...
    @staticmethod
    def create_from_dict(lookup) -> Purchase: ...
