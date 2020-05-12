# (generated with --quick)

from typing import Any, Dict

BeautifulSoup: Any
MOVIE_INFO_CACHE: Dict[Any, MovieInfo]
arrow: Any
boto3: Any
logger: logging.Logger
logging: module
requests: module

class MovieInfo:
    id: Any
    is_imax: Any
    name: Any
    release_date: Any
    def __init__(self, movie_code, name, release_date, is_imax) -> None: ...
    def __repr__(self) -> str: ...

def get_movie_info(movie_code) -> MovieInfo: ...
def is_imax_movie(movie_code) -> Any: ...
def save_movie_info(movie_info) -> None: ...
