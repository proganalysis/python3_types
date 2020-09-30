# (generated with --quick)

import requests.sessions
from typing import Any, Dict

APIC: Any
EasyMP3: Any
MP3: Any
TIT1: Any
TIT2: Any
USLT: Any
__version__: Any
logging: module
mock: module
os: module
print_clean: Any
requests: module
requests_patch: Any
slugify: Any
sys: module

class BandcampDownloader:
    album_art: Any
    debugging: Any
    directory: Any
    embed_art: Any
    embed_lyrics: Any
    grouping: Any
    headers: Dict[str, str]
    no_slugify: Any
    num_tracks: int
    overwrite: Any
    session: requests.sessions.Session
    template: Any
    track_num: int
    urls: Any
    def __init__(self, template, directory, overwrite, embed_lyrics, grouping, embed_art, no_slugify, debugging, urls = ...) -> None: ...
    @staticmethod
    def create_directory(filename: str) -> str: ...
    def download_album(self, album: dict) -> bool: ...
    def start(self, album: dict) -> None: ...
    def template_to_path(self, track: dict) -> str: ...
    def write_id3_tags(self, filepath: str, meta: dict) -> None: ...
