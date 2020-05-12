# (generated with --quick)

import abc
import enum
import pathlib
from typing import Any, Callable, List, Optional, Tuple, Type, TypeVar

ABCMeta: Type[abc.ABCMeta]
Enum: Type[enum.Enum]
Path: Type[pathlib.Path]
audioread: Any
dot: Any
lazy: Any
librosa: Any
log: Any
math: module
mean: Any
mkdir: Any
name_without_extension: Any
ndarray: Type[numpy.ndarray]
numpy: module
os: module
std: Any
vectorize: Any
write_text: Any

_FuncT = TypeVar('_FuncT', bound=Callable)
_TPositionalLabel = TypeVar('_TPositionalLabel', bound=PositionalLabel)

class CachedLabeledSpectrogram(LabeledSpectrogram):
    id: str
    label: str
    original: LabeledSpectrogram
    spectrogram_cache_file: pathlib.Path
    def __init__(self, original: LabeledSpectrogram, spectrogram_cache_directory: pathlib.Path) -> None: ...
    def _calculate_and_save_spectrogram(self) -> numpy.ndarray: ...
    def _load_from_cache(self) -> Any: ...
    def _save_to_cache(self, spectrogram: numpy.ndarray) -> None: ...
    def is_cached(self) -> bool: ...
    def move_incorrect_cached_file_to_backup_location_and_save_error(self, error_text: str) -> None: ...
    def repair_cached_file_if_incorrect(self) -> None: ...
    def z_normalized_transposed_spectrogram(self) -> numpy.ndarray: ...

class LabeledExample(LabeledSpectrogram):
    duration_in_s: Any
    fourier_window_length: int
    get_raw_audio: Callable[[], numpy.ndarray]
    hop_length: int
    id: str
    label: str
    label_with_tags: Any
    mel_frequency_count: int
    positional_label: Any
    sample_rate: int
    def __init__(self, get_raw_audio: Callable[[], numpy.ndarray], sample_rate: int = ..., id: Optional[str] = ..., label: Optional[str] = ..., fourier_window_length: int = ..., hop_length: int = ..., mel_frequency_count: int = ..., label_with_tags: Optional[str] = ..., positional_label: Optional[PositionalLabel] = ...) -> None: ...
    def __str__(self) -> str: ...
    def _amplitude_spectrogram(self) -> numpy.ndarray: ...
    def _complex_spectrogram(self) -> numpy.ndarray: ...
    def _convert_spectrogram_to_mel_scale(self, linear_frequency_spectrogram: numpy.ndarray) -> numpy.ndarray: ...
    @staticmethod
    def _power_level_from_power_spectrogram(spectrogram: numpy.ndarray) -> numpy.ndarray: ...
    def _power_spectrogram(self) -> numpy.ndarray: ...
    def frequency_count_from_spectrogram(self, spectrogram: numpy.ndarray) -> int: ...
    def highest_detectable_frequency(self) -> float: ...
    def mel_frequencies(self) -> List[float]: ...
    def reconstructed_audio_from_spectrogram(self) -> numpy.ndarray: ...
    def spectrogram(self, type: SpectrogramType = ..., frequency_scale: SpectrogramFrequencyScale = ...) -> numpy.ndarray: ...
    def tag_count(self, tag: str) -> int: ...
    def time_step_count(self) -> int: ...
    def time_step_rate(self) -> float: ...
    def z_normalized_transposed_spectrogram(self) -> numpy.ndarray: ...

class LabeledExampleFromFile(LabeledExample):
    audio_directory: pathlib.Path
    audio_file: pathlib.Path
    duration_in_s: Any
    fourier_window_length: int
    get_raw_audio: Callable[[], numpy.ndarray]
    hop_length: int
    id: str
    label: str
    label_with_tags: Optional[str]
    mel_frequency_count: int
    original_sample_rate: Any
    positional_label: Optional[PositionalLabel]
    sample_rate: int
    def __init__(self, audio_file: pathlib.Path, id: Optional[str] = ..., sample_rate_to_convert_to: int = ..., label: Optional[str] = ..., fourier_window_length: int = ..., hop_length: int = ..., mel_frequency_count: int = ..., label_with_tags: Optional[str] = ..., positional_label: Optional[PositionalLabel] = ...) -> None: ...
    @staticmethod
    def file_sample_rate(audio_file: pathlib.Path) -> int: ...
    def sections(self) -> Optional[List[LabeledExample]]: ...

class LabeledSpectrogram(metaclass=abc.ABCMeta):
    __metaclass__: Type[abc.ABCMeta]
    id: str
    label: str
    def __init__(self, id: str, label: str) -> None: ...
    @abstractmethod
    def z_normalized_transposed_spectrogram(self) -> numpy.ndarray: ...

class PositionalLabel:
    label: str
    labeled_sections: List[Tuple[str, Tuple[float, float]]]
    labels: Any
    def __init__(self, labeled_sections: List[Tuple[str, Tuple[float, float]]]) -> None: ...
    def convert_range_to_seconds(self: _TPositionalLabel, original_sample_rate: int) -> _TPositionalLabel: ...
    @staticmethod
    def deserialize(serialized: str) -> PositionalLabel: ...
    def serialize(self) -> str: ...
    def with_corrected_labels(self: _TPositionalLabel, correction: Callable[[str], str]) -> _TPositionalLabel: ...

class SpectrogramFrequencyScale(enum.Enum):
    linear: str
    mel: str

class SpectrogramType(enum.Enum):
    amplitude: str
    power: str
    power_level: str

def abstractmethod(callable: _FuncT) -> _FuncT: ...
def z_normalize(array: numpy.ndarray) -> numpy.ndarray: ...
