# (generated with --quick)

from typing import List, Pattern

re: module
tag_re: Pattern[str]
tag_split_re: Pattern[str]
textwrap: module
w: StyleTagsAwareTextWrapper

class StyleTagsAwareTextWrapper(textwrap.TextWrapper):
    __doc__: str
    def _wrap_chunks(self, chunks) -> List[str]: ...
