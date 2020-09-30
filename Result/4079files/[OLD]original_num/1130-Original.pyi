# (generated with --quick)

from typing import Any, Coroutine, List, Tuple

CONF_API_KEY: Any
CONF_CODEC: str
CONF_EMOTION: str
CONF_LANG: Any
CONF_SPEED: str
CONF_VOICE: str
DEFAULT_CODEC: str
DEFAULT_EMOTION: str
DEFAULT_LANG: str
DEFAULT_SPEED: int
DEFAULT_VOICE: str
MAX_SPEED: int
MIN_SPEED: float
PLATFORM_SCHEMA: Any
Provider: Any
SUPPORTED_EMOTION: List[str]
SUPPORTED_OPTIONS: List[str]
SUPPORT_CODECS: List[str]
SUPPORT_LANGUAGES: List[str]
SUPPORT_VOICES: List[str]
YANDEX_API_URL: str
_LOGGER: logging.Logger
aiohttp: Any
async_get_clientsession: Any
async_timeout: Any
asyncio: module
cv: Any
logging: module
vol: Any

class YandexSpeechKitProvider(Any):
    __doc__: str
    _codec: Any
    _emotion: Any
    _key: Any
    _language: Any
    _speaker: Any
    _speed: str
    default_language: Any
    hass: Any
    name: str
    supported_languages: List[str]
    supported_options: List[str]
    def __init__(self, hass, conf) -> None: ...
    def async_get_tts_audio(self, message, language, options = ...) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...

def async_get_engine(hass, config) -> Coroutine[Any, Any, YandexSpeechKitProvider]: ...
