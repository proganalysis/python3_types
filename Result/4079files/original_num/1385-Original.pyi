# (generated with --quick)

import collections
import enum
import fractions
import io
import numbers
import numpy
from typing import Any, Callable, Generator, Iterable, Iterator, List, Optional, Pattern, Sequence, Set, Sized, Tuple, Type, TypeVar, Union

BufferedIOBase: Type[io.BufferedIOBase]
DEVNULL: int
Enum: Type[enum.Enum]
Fraction: Type[fractions.Fraction]
MEASURE_SAMPLE_RATE: Any
Number: Type[numbers.Number]
PIPE: int
_whitespace_pattern: Pattern[str]
auto: Type[enum.auto]
chardet: module
defaultdict: Type[collections.defaultdict]
ex_ffmpeg: str
ex_ffprobe: str
itertools: module
known_audio_extensions: Set[str]
natural_sort_key: Any
np: module
os: module
path: module
re: module
sp: module
sys: module

_TAudioFileParams = TypeVar('_TAudioFileParams', bound=AudioFileParams)
_TAudioSource = TypeVar('_TAudioSource', bound=AudioSource)
_TAudioSourceInfo = TypeVar('_TAudioSourceInfo', bound=AudioSourceInfo)
_TTrackInfo = TypeVar('_TTrackInfo', bound=TrackInfo)

class AudioFileParams(tuple):
    __slots__ = ["album", "artist", "channel_count", "sample_rate", "title"]
    __dict__: collections.OrderedDict[str, Union[int, str]]
    _field_defaults: collections.OrderedDict[str, Union[int, str]]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str, str, str]
    album: str
    artist: str
    channel_count: int
    sample_rate: int
    title: str
    def __getnewargs__(self) -> Tuple[int, int, str, str, str]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TAudioFileParams], channel_count: int, sample_rate: int, title: str, artist: str, album: str) -> _TAudioFileParams: ...
    def _asdict(self) -> collections.OrderedDict[str, Union[int, str]]: ...
    @classmethod
    def _make(cls: Type[_TAudioFileParams], iterable: Iterable[Union[int, str]], new = ..., len: Callable[[Sized], int] = ...) -> _TAudioFileParams: ...
    def _replace(self: _TAudioFileParams, **kwds: Union[int, str]) -> _TAudioFileParams: ...

class AudioSource(tuple):
    __slots__ = ["blocks_generator", "samples_per_block", "source_info"]
    __dict__: collections.OrderedDict[str, Union[AudioSourceInfo, int, Iterator[Iterator[numpy.ndarray]]]]
    _field_defaults: collections.OrderedDict[str, Union[AudioSourceInfo, int, Iterator[Iterator[numpy.ndarray]]]]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str]
    blocks_generator: Iterator[Iterator[numpy.ndarray]]
    samples_per_block: int
    source_info: AudioSourceInfo
    def __getnewargs__(self) -> Tuple[AudioSourceInfo, int, Iterator[Iterator[numpy.ndarray]]]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TAudioSource], source_info: AudioSourceInfo, samples_per_block: int, blocks_generator: Iterator[Iterator[numpy.ndarray]]) -> _TAudioSource: ...
    def _asdict(self) -> collections.OrderedDict[str, Union[AudioSourceInfo, int, Iterator[Iterator[numpy.ndarray]]]]: ...
    @classmethod
    def _make(cls: Type[_TAudioSource], iterable: Iterable[Union[AudioSourceInfo, int, Iterator[Iterator[numpy.ndarray]]]], new = ..., len: Callable[[Sized], int] = ...) -> _TAudioSource: ...
    def _replace(self: _TAudioSource, **kwds: Union[AudioSourceInfo, int, Iterator[Iterator[numpy.ndarray]]]) -> _TAudioSource: ...

class AudioSourceInfo(tuple):
    __slots__ = ["album", "channel_count", "name", "path", "performers", "sample_rate", "tracks"]
    __dict__: collections.OrderedDict[str, Union[int, str, List[TrackInfo], Sequence[str]]]
    _field_defaults: collections.OrderedDict[str, Union[int, str, List[TrackInfo], Sequence[str]]]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str, str, str, str, str]
    album: str
    channel_count: int
    name: str
    path: str
    performers: Sequence[str]
    sample_rate: int
    tracks: List[TrackInfo]
    def __getnewargs__(self) -> Tuple[str, str, Sequence[str], str, int, int, List[TrackInfo]]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TAudioSourceInfo], path: str, name: str, performers: Sequence[str], album: str, channel_count: int, sample_rate: int, tracks: List[TrackInfo]) -> _TAudioSourceInfo: ...
    def _asdict(self) -> collections.OrderedDict[str, Union[int, str, List[TrackInfo], Sequence[str]]]: ...
    @classmethod
    def _make(cls: Type[_TAudioSourceInfo], iterable: Iterable[Union[int, str, List[TrackInfo], Sequence[str]]], new = ..., len: Callable[[Sized], int] = ...) -> _TAudioSourceInfo: ...
    def _replace(self: _TAudioSourceInfo, **kwds: Union[int, str, List[TrackInfo], Sequence[str]]) -> _TAudioSourceInfo: ...

class CueCmd(enum.Enum):
    EOF: enum.auto
    FILE: enum.auto
    INDEX: enum.auto
    PERFORMER: enum.auto
    TITLE: enum.auto
    TRACK: enum.auto

class FileKind(enum.Enum):
    AUDIO: enum.auto
    CUE: enum.auto
    FOLDER: enum.auto

class TrackInfo(tuple):
    __slots__ = ["global_index", "name", "offset_samples"]
    __dict__: collections.OrderedDict[str, Union[int, str]]
    _field_defaults: collections.OrderedDict[str, Union[int, str]]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str]
    global_index: int
    name: str
    offset_samples: int
    def __getnewargs__(self) -> Tuple[int, str, int]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TTrackInfo], global_index: int, name: str, offset_samples: int) -> _TTrackInfo: ...
    def _asdict(self) -> collections.OrderedDict[str, Union[int, str]]: ...
    @classmethod
    def _make(cls: Type[_TTrackInfo], iterable: Iterable[Union[int, str]], new = ..., len: Callable[[Sized], int] = ...) -> _TTrackInfo: ...
    def _replace(self: _TTrackInfo, **kwds: Union[int, str]) -> _TTrackInfo: ...

def _audio_source_from_file(in_path, track_index = ...) -> AudioSourceInfo: ...
def _audio_sources_from_folder(in_path) -> Iterable[AudioSourceInfo]: ...
def _get_audio_properties(in_path) -> AudioFileParams: ...
def _get_params(in_path) -> AudioFileParams: ...
def _parse_audio_params(s) -> AudioFileParams: ...
def _parse_cue_cmd(line: str) -> Optional[tuple]: ...
def _read_audio_blocks(in_path, channel_count, samples_per_block, tracks: List[TrackInfo]) -> Iterator[Iterator[numpy.ndarray]]: ...
def _test_ffmpeg() -> None: ...
def _translate_from_cue(directory_path, cue_items) -> Iterable[AudioSourceInfo]: ...
def _unquote(s: str) -> str: ...
def get_file_kind(in_path: str) -> FileKind: ...
def parse_cd_time(offset: str) -> numbers.Number: ...
def parse_cue(in_path) -> Generator[nothing, Any, nothing]: ...
def read_audio_data(what: AudioSourceInfo, samples_per_block: int) -> AudioSource: ...
def read_audio_info(in_path: str) -> Iterable[AudioSourceInfo]: ...
