from homeassistant.components.tts import Provider
from typing import Any, Optional

_LOGGER: Any
YANDEX_API_URL: str
SUPPORT_LANGUAGES: Any
SUPPORT_CODECS: Any
SUPPORT_VOICES: Any
SUPPORTED_EMOTION: Any
MIN_SPEED: float
MAX_SPEED: int
CONF_CODEC: str
CONF_VOICE: str
CONF_EMOTION: str
CONF_SPEED: str
DEFAULT_LANG: str
DEFAULT_CODEC: str
DEFAULT_VOICE: str
DEFAULT_EMOTION: str
DEFAULT_SPEED: int
SUPPORTED_OPTIONS: Any

async def async_get_engine(hass: Any, config: Any): ...

class YandexSpeechKitProvider(Provider):
    hass: Any = ...
    _codec: Any = ...
    _key: Any = ...
    _speaker: Any = ...
    _language: Any = ...
    _emotion: Any = ...
    _speed: Any = ...
    name: str = ...
    def __init__(self, hass: Any, conf: Any) -> None: ...
    @property
    def default_language(self): ...
    @property
    def supported_languages(self): ...
    @property
    def supported_options(self): ...
    async def async_get_tts_audio(self, message: Any, language: Any, options: Optional[Any] = ...): ...