# (generated with --quick)

from typing import Any, Dict

EMPTY_DTM_MESSAGE: Any
SEG_NON_POSITIVE_MESSAGE: Any
TopwordAnalysisType: Any
TopwordModel: Any
TopwordTestOptions: Any
np: module
pd: Any
test_class_division_map_all_to_para: Any
test_class_division_map_class_to_class: Any
test_class_division_map_class_to_para: Any
test_dtm_all_to_para: Any
test_dtm_class_to_class: Any
test_dtm_class_to_para: Any
test_front_end_option_all_to_para: Any
test_front_end_option_class_to_class: Any
test_front_end_option_class_to_para: Any
test_id_temp_label_map_all_to_para: Dict[int, str]
test_id_temp_label_map_class_to_class: Dict[int, str]
test_id_temp_label_map_class_to_para: Dict[int, str]
test_option_all_to_para: Any
test_option_class_to_class: Any
test_option_class_to_para: Any
test_option_empty_all_to_para: Any
test_option_empty_class_to_class: Any
test_option_empty_class_to_para: Any
test_results_all_to_para: Any
test_results_class_to_class: Any
test_results_class_to_para: Any
test_topword_model_all_to_para: Any
test_topword_model_empty_all_to_para: Any
test_topword_model_empty_one_class_to_para: Any
test_topword_model_empty_two_class_to_class: Any
test_topword_model_one_class_to_para: Any
test_topword_model_two_class_to_class: Any

class TestClassToAll:
    def test_normal_case_result(self) -> None: ...
    def test_special_case(self) -> None: ...

class TestClassToClass:
    def test_normal_case_result(self) -> None: ...
    def test_special_case(self) -> None: ...

class TestParaToGroup:
    def test_normal_case_result(self) -> None: ...
    def test_special_case(self) -> None: ...

class TestZTest:
    def test_normal_case(self) -> None: ...
    def test_special_case(self) -> None: ...
