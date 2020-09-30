# (generated with --quick)

from typing import Any, Dict, List, Union

EXPECTED_PATHS: List[List[List[str]]]
EXPECTED_VALUES: List[List[str]]
SAMPLE_OBJECTS: List[Dict[str, Union[str, Dict[str, Union[str, Dict[str, str]]]]]]
copy: module
factories: Any
freeze_time: Any
logging: module
models: Any
nested_data: Any
pytest: Any
random: module
test_node_path_map_caching: Any
transformers: Any
types: module
utc_now: Any

def _verify_logged_metrics(mock_logger, expected_submissions_processed) -> None: ...
def test_json_transform_to_dict(session, raw_data, transformer) -> None: ...
def test_json_transform_to_model(session, raw_data, transformer, mock_logger) -> None: ...
def test_map_nested(nested_data: tuple) -> None: ...
