import pandas as pd

def make_bin_edges(data: pd.DataFrame, col: str) -> pd.DataFrame: ...
def test_1d_interpolation() -> None: ...
def test_age_year_interpolation() -> None: ...
def test_interpolation_called_missing_key_col() -> None: ...
def test_interpolation_called_missing_param_col() -> None: ...
def test_2d_interpolation() -> None: ...
def test_interpolation_with_categorical_parameters() -> None: ...
def test_order_zero_2d() -> None: ...
def test_order_zero_2d_fails_on_extrapolation() -> None: ...
def test_order_zero_1d_no_extrapolation() -> None: ...
def test_order_zero_1d_constant_extrapolation() -> None: ...
def test_validate_parameters__empty_data() -> None: ...
def test_check_data_complete_gaps() -> None: ...
def test_check_data_complete_overlap() -> None: ...
def test_check_data_missing_combos() -> None: ...
def test_order0interp() -> None: ...
def test_order_zero_1d_with_key_column() -> None: ...
def test_order_zero_non_numeric_values() -> None: ...
def test_order_zero_3d_with_key_col() -> None: ...
def test_order_zero_diff_bin_sizes() -> None: ...
def test_order_zero_given_call_column() -> None: ...
