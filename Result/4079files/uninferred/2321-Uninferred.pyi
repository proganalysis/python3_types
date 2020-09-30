from typing import Any

test_munge_input: str
test_munge_count: int
test_munge_result_a: str
test_munge_result_b: str
test_format_formats: Any
test_format_data: Any
test_format_result: str
test_pluralize_num_a: int
test_pluralize_num_b: int
test_pluralize_result_a: str
test_pluralize_result_b: str
test_pluralize_text: str
test_strip_colors_input: str
test_strip_colors_result: str
test_truncate_str_input: str
test_truncate_str_length_a: int
test_truncate_str_length_b: int
test_truncate_str_result_a: str
test_truncate_str_result_b: str
test_truncate_words_input: str
test_truncate_words_length_a: int
test_truncate_words_length_b: int
test_truncate_words_result_a: str
test_truncate_words_result_b: str
test_strip_html_input: str
test_strip_html_result: str
test_multiword_replace_dict: Any
test_multiword_replace_text: str
test_multiword_replace_result: str
test_ireplace_input: str
test_chunk_str_input: str
test_chunk_str_result: Any

def test_munge() -> None: ...
def test_dict_format() -> None: ...
def test_pluralize() -> None: ...
def test_auto_pluralize(item: Any, count: Any, output: Any) -> None: ...
def test_strip_colors() -> None: ...
def test_truncate_str() -> None: ...
def test_truncate_words() -> None: ...
def test_strip_html() -> None: ...
def test_multiword_replace() -> None: ...
def test_ireplace() -> None: ...
def test_chunk_str() -> None: ...
def test_get_text_list() -> None: ...
def test_smart_split() -> None: ...
def test_gen_md_table() -> None: ...
