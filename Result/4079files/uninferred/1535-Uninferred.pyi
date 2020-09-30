from KINCluster.core.pipeline import Pipeline
from KINCluster.lib.tokenizer import stemize as stemize, tokenize as tokenize
from typing import Any

test_text: Any
test_keyword: Any

class Pipeline(Pipeline):
    def capture_item(self) -> None: ...
    def dress_item(self, items: Any) -> None: ...

def test_cluster1() -> None: ...
