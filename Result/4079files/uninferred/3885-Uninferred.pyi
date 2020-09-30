from typing import Any

CLIENT_ID: Any
CLIENT_SECRET: Any
REFRESH_TOKEN: Any
FRANK_ZAPPA: str

def spotify_auth(): ...
def ccspotify(spotify_auth: Any): ...
def test_get_artist(ccspotify: Any) -> None: ...
