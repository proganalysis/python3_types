# (generated with --quick)

import contentviews.base
from typing import Any, Generator, List, Optional, Tuple

base: module
multidict: Any
url: Any

class ViewURLEncoded(contentviews.base.View):
    content_types: List[str]
    name: str
    def __call__(self, data, **metadata) -> Optional[Tuple[str, Generator[List[Tuple[str, Any]], Any, None]]]: ...
