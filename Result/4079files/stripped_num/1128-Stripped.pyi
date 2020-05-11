# (generated with --quick)

import abc
import enum
import pathlib
from typing import Any, Callable, Optional, Type, TypeVar

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
    id: Any
    label: Any
    original: Any
    spectrogram_cache_file: Any
    def __init__(self, original, spectrogram_cache_directory) -> None: ...
    def _calculate_and_save_spectrogram(self) -> Any: ...
    def _load_from_cache(self) -> Any: ...
    def _save_to_cache(self, spectrogram) -> None: ...
    def is_cached(self) -> Any: ...
    def move_incorrect_cached_file_to_backup_location_and_save_error(self, error_text) -> None: ...
    def repair_cached_file_if_incorrect(self) -> None: ...
    def z_normalized_transposed_spectrogram(self) -> Any: ...

class LabeledExample(LabeledSpectrogram):
    duration_in_s: Any
    fourier_window_length: Any
    get_raw_audio: Any
    hop_length: Any
    id: Any
    label: Any
    label_with_tags: Any
    mel_frequency_count: Any
    positional_label: Any
    sample_rate: Any
    def __init__(self, get_raw_audio, sample_rate = ..., id = ..., label = ..., fourier_window_length = ..., hop_length = ..., mel_frequency_count = ..., label_with_tags = ..., positional_label = ...) -> None: ...
    def __str__(self) -> Any: ...
    def _amplitude_spectrogram(self) -> Any: ...
    def _complex_spectrogram(self) -> Any: ...
    def _convert_spectrogram_to_mel_scale(self, linear_frequency_spectrogram) -> Any: ...
    @staticmethod
    def _power_level_from_power_spectrogram(spectrogram) -> Any: ...
    def _power_spectrogram(self) -> Any: ...
    def frequency_count_from_spectrogram(self, spectrogram) -> Any: ...
    def highest_detectable_frequency(self) -> Any: ...
    def mel_frequencies(self) -> Any: ...
    def reconstructed_audio_from_spectrogram(self) -> Any: ...
    def spectrogram(self, type = ..., frequency_scale = ...) -> Any: ...
    def tag_count(self, tag) -> Any: ...
    def time_step_count(self) -> Any: ...
    def time_step_rate(self) -> Any: ...
    def z_normalized_transposed_spectrogram(self) -> Any: ...

class LabeledExampleFromFile(LabeledExample):
    audio_directory: pathlib.Path
    audio_file: Any
    duration_in_s: Any
    fourier_window_length: Any
    get_raw_audio: Callable[[], Any]
    hop_length: Any
    id: Any
    label: Any
    label_with_tags: Any
    mel_frequency_count: Any
    original_sample_rate: Any
    positional_label: Any
    sample_rate: Any
    def __init__(self, audio_file, id = ..., sample_rate_to_convert_to = ..., label = ..., fourier_window_length = ..., hop_length = ..., mel_frequency_count = ..., label_with_tags = ..., positional_label = ...) -> None: ...
    @staticmethod
    def file_sample_rate(audio_file) -> Any: ...
    def sections(self) -> Optional[list]: ...

class LabeledSpectrogram(metaclass=abc.ABCMeta):
    __metaclass__: Type[abc.ABCMeta]
    id: Any
    label: Any
    def __init__(self, id, label) -> None: ...
    @abstractmethod
    def z_normalized_transposed_spectrogram(self) -> Any: ...

class PositionalLabel:
    label: str
    labeled_sections: Any
    labels: Any
    def __init__(self, labeled_sections) -> None: ...
    def convert_range_to_seconds(self: _TPositionalLabel, original_sample_rate) -> _TPositionalLabel: ...
    @staticmethod
    def deserialize(serialized) -> PositionalLabel: ...
    def serialize(self) -> str: ...
    def with_corrected_labels(self: _TPositionalLabel, correction) -> _TPositionalLabel: ...

class SpectrogramFrequencyScale(enum.Enum):
    linear: str
    mel: str

class SpectrogramType(enum.Enum):
    amplitude: str
    power: str
    power_level: str

def abstractmethod(callable: _FuncT) -> _FuncT: ...
def z_normalize(array) -> Any: ...
