# (generated with --quick)

import extractors.core
from typing import Dict, List, Type

Extractor: Type[extractors.core.Extractor]
np: module

class MedianBRP(extractors.core.Extractor):
    __doc__: str
    data: List[str]
    features: List[str]
    def fit(self, magnitude) -> Dict[str, float]: ...
