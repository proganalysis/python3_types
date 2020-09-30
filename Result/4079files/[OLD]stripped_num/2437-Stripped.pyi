# (generated with --quick)

from typing import Any, Dict, Generic, List, Optional, Tuple, Type, TypeVar

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
_T0 = TypeVar('_T0')

class Album(BaseModel):
    __doc__: str
    album_name: Any
    artist: Any
    id: Any
    tracks: list
    def __init__(self, id, album_name, artist, tracks = ...) -> None: ...

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
    def create(self, validated_data: _T0) -> _T0: ...

class Artist(BaseModel):
    __doc__: str
    first_name: Any
    id: Any
    last_name: Any
    def __init__(self, id, first_name, last_name) -> None: ...
    def update(self, id, first_name, last_name) -> None: ...

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
    def create(self, validated_data: _T0) -> _T0: ...
    def update(self, instance: _T0, validated_data) -> _T0: ...

class BaseModel:
    __doc__: str
    pk: Any
    def serializable_value(self, field_name) -> Any: ...

class QuerySet(Generic[T]):
    __doc__: str
    objs: Any
    def __getitem__(self: QuerySet[nothing], item) -> Any: ...
    def __init__(self: QuerySet[nothing], objs) -> None: ...
    def __iter__(self: QuerySet[nothing]) -> Any: ...
    def add(self: QuerySet[nothing], obj) -> None: ...
    def count(self: QuerySet[nothing]) -> int: ...
    def get(self: QuerySet[nothing], pk) -> Any: ...

class Track(BaseModel):
    __doc__: str
    album: Any
    id: Any
    name: Any
    track_num: Any
    def __init__(self, id, track_num, name, album) -> None: ...

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
def get_albums() -> QuerySet[nothing]: ...
def get_artists() -> QuerySet[nothing]: ...
def get_tracks() -> QuerySet[nothing]: ...
def reset_data() -> None: ...
