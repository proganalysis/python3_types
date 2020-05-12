# (generated with --quick)

from typing import Any, Dict, Generic, Iterator, List, Optional, Tuple, Type, TypeVar

ALBUMS: Any
ARTISTS: Any
CamelCaseTransform: Any
INITIAL_ALBUMS: List[Album]
INITIAL_ARTISTS: List[Artist]
INITIAL_TRACKS: List[Track]
JSONAPIRelationshipField: Any
ResourceObject: Any
TRACKS: Any
serializers: Any

T = TypeVar('T')
_T = TypeVar('_T')

class Album(BaseModel):
    __doc__: str
    album_name: str
    artist: Any
    id: int
    tracks: List[Track]
    def __init__(self, id: int, album_name: str, artist: Optional[Artist], tracks: Optional[List[Track]] = ...) -> None: ...

class AlbumObject(Any):
    __doc__: str
    attributes: Tuple[str]
    relationships: Tuple[str, str]
    transformer: Any
    type: str

class AlbumSerializer(Any):
    __doc__: str
    album_name: Any
    artist: Any
    id: Any
    schema: Type[AlbumObject]
    tracks: Any
    def create(self, validated_data: dict) -> dict: ...

class Artist(BaseModel):
    __doc__: str
    first_name: str
    id: int
    last_name: str
    def __init__(self, id: int, first_name: str, last_name: str) -> None: ...
    def update(self, id: int, first_name: str, last_name: str) -> None: ...

class ArtistObject(Any):
    __doc__: str
    attributes: Tuple[str, str]
    transformer: Any
    type: str

class ArtistSerializer(Any):
    __doc__: str
    first_name: Any
    id: Any
    last_name: Any
    schema: Type[ArtistObject]
    def create(self, validated_data: dict) -> dict: ...
    def update(self, instance: Artist, validated_data: dict) -> Artist: ...

class BaseModel:
    __doc__: str
    id: int
    pk: int
    def serializable_value(self, field_name: str) -> Any: ...

class QuerySet(Generic[T]):
    __doc__: str
    objs: list
    def __getitem__(self, item: int) -> T: ...
    def __init__(self, objs: List[T]) -> None: ...
    def __iter__(self) -> Iterator[T]: ...
    def add(self, obj: T) -> None: ...
    def count(self) -> int: ...
    def get(self, pk: int) -> T: ...

class Track(BaseModel):
    __doc__: str
    album: Album
    id: int
    name: str
    track_num: int
    def __init__(self, id: int, track_num: int, name: str, album: Album) -> None: ...

class TrackObject(Any):
    __doc__: str
    attributes: Tuple[str, str]
    relationships: Tuple[str]
    transformer: Any
    type: str

class TrackSerializer(Any):
    __doc__: str
    album: Any
    id: Any
    name: Any
    schema: Type[TrackObject]
    track_num: Any

def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
def get_albums() -> QuerySet: ...
def get_artists() -> QuerySet: ...
def get_tracks() -> QuerySet: ...
def reset_data() -> None: ...
