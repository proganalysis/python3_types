from typing import Any

_max_line_size: Any
max_line_size: Any
line_delimited_data: Any

def test_yields_lines(max_line_size: Any, data: Any): ...
def test_too_large_line_raises(max_line_size: Any, over_by: Any): ...
def test_truncated_line_raises(truncated_data: Any): ...

_lines_of_line_delimited_data: Any
lines_of_line_delimited_data: Any

def test_skips_none_return_callback(data: Any, skipped: Any): ...
