# (generated with --quick)

from typing import Any

BeautifulSoup: Any
checks: Any
commands: Any
urllib: module

class Words(Any):
    antonym: Any
    bot: Any
    define: Any
    pronunciation: Any
    rhyme: Any
    spellcheck: Any
    synonym: Any
    translate: Any
    translate_from: Any
    translate_languages: Any
    translate_to: Any
    def __init__(self, bot) -> None: ...
    def process_translate(self, ctx, text, to_language_code, from_language_code = ...) -> coroutine: ...

def setup(bot) -> None: ...
