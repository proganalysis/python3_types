# (generated with --quick)

from typing import Any

Container: Any
CronTrigger: Any
DateTrigger: Any
IntervalTrigger: Any
JobConfigValidator: Any
_parse_flags: Any
mark: Any
parse_labels: Any
test_flags: Any
test_options_parsing: Any

def test_interval_trigger() -> None: ...
def test_parse_labels(cfg, mocker) -> None: ...
def test_parse_labels_with_time_units(cfg, mocker) -> None: ...
def test_parse_labels_with_user_option(cfg, mocker) -> None: ...
def test_parse_labels_with_user_option_from_image(cfg, mocker) -> None: ...
