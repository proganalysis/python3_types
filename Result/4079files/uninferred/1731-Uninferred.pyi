from collections import namedtuple
from typing import Any

Finals = namedtuple('Finals', ['pinyin', 'rhyme', 'tones'])

def finals_info(word: Any): ...
