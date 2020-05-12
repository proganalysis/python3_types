import textwrap
from typing import Any, List

tag_split_re: Any
tag_re: Any

class StyleTagsAwareTextWrapper(textwrap.TextWrapper):
    def _wrap_chunks(self, chunks: List[str]) -> List[str]: ...
