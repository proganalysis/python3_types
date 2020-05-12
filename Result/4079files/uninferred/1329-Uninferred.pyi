from contextlib import contextmanager as contextmanager
from diffutils.api import diff as diff, parse_unified_diff as parse_unified_diff
from diffutils.output import generate_unified_diff as generate_unified_diff
from typing import Any

test_data: Any
bench_methods: Any
__cached_test_data_lines: Any

def test_data_lines(name: Any, data_dir: str = ...): ...
def main() -> None: ...
