# (generated with --quick)

import contentviews.base
from typing import Any, Iterator, List, Optional, Tuple, Union

base: module
multidict: Any
url: Any

class ViewURLEncoded(contentviews.base.View):
    content_types: List[str]
    name: str
    def __call__(self, data, **metadata) -> Optional[Tuple[str, Iterator[List[Tuple[str, Union[bytes, str]]]]]]: ...
