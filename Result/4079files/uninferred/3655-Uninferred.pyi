from typing import Any

class TestZTest:
    def test_normal_case(self) -> None: ...
    def test_special_case(self) -> None: ...

test_dtm_all_to_para: Any
test_front_end_option_all_to_para: Any
test_id_temp_label_map_all_to_para: Any
test_class_division_map_all_to_para: Any
test_option_all_to_para: Any
test_topword_model_all_to_para: Any
test_results_all_to_para: Any
test_option_empty_all_to_para: Any
test_topword_model_empty_all_to_para: Any

class TestParaToGroup:
    def test_normal_case_result(self) -> None: ...
    def test_special_case(self) -> None: ...

test_dtm_class_to_para: Any
test_id_temp_label_map_class_to_para: Any
test_front_end_option_class_to_para: Any
test_class_division_map_class_to_para: Any
test_option_class_to_para: Any
test_topword_model_one_class_to_para: Any
test_results_class_to_para: Any
test_option_empty_class_to_para: Any
test_topword_model_empty_one_class_to_para: Any

class TestClassToAll:
    def test_normal_case_result(self) -> None: ...
    def test_special_case(self) -> None: ...

test_dtm_class_to_class: Any
test_id_temp_label_map_class_to_class: Any
test_front_end_option_class_to_class: Any
test_class_division_map_class_to_class: Any
test_option_class_to_class: Any
test_topword_model_two_class_to_class: Any
test_results_class_to_class: Any
test_option_empty_class_to_class: Any
test_topword_model_empty_two_class_to_class: Any

class TestClassToClass:
    def test_normal_case_result(self) -> None: ...
    def test_special_case(self) -> None: ...
