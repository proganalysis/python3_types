# (generated with --quick)

import datetime
from typing import Any, Dict, Type

BandcampJSON: Any
BeautifulSoup: Any
FeatureNotFound: Any
__version__: Any
dt: Type[datetime.datetime]
json: module
logging: module
requests: module

class Bandcamp:
    headers: Dict[str, str]
    soup: Any
    tracks: Any
    def __init__(self) -> None: ...
    def all_tracks_available(self) -> bool: ...
    @staticmethod
    def generate_album_url(artist: str, slug: str, page_type: str) -> str: ...
    def get_album_art(self) -> str: ...
    def get_track_lyrics(self, track_url) -> Any: ...
    @staticmethod
    def get_track_metadata(track: dict) -> dict: ...
    def parse(self, url: str, art: bool = ..., lyrics: bool = ..., debugging: bool = ...) -> dict: ...
