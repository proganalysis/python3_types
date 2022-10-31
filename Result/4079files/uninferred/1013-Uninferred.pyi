from typing import Any

class SubmoduleBaseclass:
    name: str = ...
    results: Any = ...
    summary: Any = ...
    def __init__(self) -> None: ...
    def get_name(self): ...
    def build_taxonomy(self, level: Any, namespace: Any, predicate: Any, value: Any): ...
    def check_file(self, **kwargs: Any): ...
    def analyze_file(self, path: Any): ...
    def module_summary(self): ...
    def add_result_subsection(self, subsection_header: Any, results: Any) -> None: ...