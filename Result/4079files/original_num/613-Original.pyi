# (generated with --quick)

from typing import Any, Coroutine

Image: module
ImageColorGenerator: Any
WCloud: Any
aiohttp: Any
asyncio: module
checks: Any
commands: Any
converter: Any
dataIO: Any
discord: Any
errors: Any
formatter: Any
functools: module
np: module
os: module
send_cmd_help: module

class WordCloud:
    __doc__: str
    _wcset_bgcolor: Any
    _wcset_clearmask: Any
    _wcset_clearwords: Any
    _wcset_colormask: Any
    _wcset_exclude: Any
    _wcset_listmask: Any
    _wcset_maskfile: Any
    _wcset_maxwords: Any
    _wcset_upload: Any
    bot: Any
    mask_folder: str
    session: Any
    settings: Any
    settings_path: str
    wcset: Any
    wordcloud: Any
    def _WordCloud__unload(self) -> None: ...
    def __init__(self, bot) -> None: ...
    def _list_masks(self, ctx) -> Coroutine[Any, Any, None]: ...
    @staticmethod
    def generate(filepath, text, **kwargs) -> None: ...

def check_files() -> None: ...
def check_folders() -> None: ...
def setup(bot) -> None: ...
