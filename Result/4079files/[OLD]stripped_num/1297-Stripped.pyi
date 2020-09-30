# (generated with --quick)

import datetime
from typing import Any, Dict, Optional, Type

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
    def generate_album_url(artist, slug, page_type) -> str: ...
    def get_album_art(self) -> Any: ...
    def get_track_lyrics(self, track_url) -> Any: ...
    @staticmethod
    def get_track_metadata(track) -> Dict[str, Any]: ...
    def parse(self, url, art = ..., lyrics = ..., debugging = ...) -> Optional[Dict[str, Any]]: ...
