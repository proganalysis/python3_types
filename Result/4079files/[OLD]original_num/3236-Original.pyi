# (generated with --quick)

from typing import Any, Dict, List, Union

MetaParam: Any
is_string: Any
parse_value: Any
string_to_float: Any
taxcalc: Any

class TaxCalcField(object):
    __doc__: str
    default_value: str
    id: Any
    label: Any
    param: Any
    values: Any
    values_by_year: Dict[Any, str]
    def __init__(self, id, label, values, param, first_budget_year, meta_param = ...) -> None: ...

class TaxCalcParam(object):
    FORM_HIDDEN_PARAMS: List[str]
    __doc__: str
    col_fields: List[TaxCalcField]
    coming_soon: bool
    cpi_field: TaxCalcField
    gray_out: bool
    hidden: bool
    inflatable: Any
    info: str
    max: Any
    min: Any
    name: Any
    nice_id: Any
    start_year: Any
    tc_id: Any
    def _TaxCalcParam__load_from_json(self, param_id, attributes, first_budget_year, use_puf_not_cps) -> None: ...
    def __init__(self, param_id, attributes, first_budget_year, use_puf_not_cps = ...) -> None: ...

def default_behavior(first_budget_year) -> Dict[Any, TaxCalcParam]: ...
def default_policy(first_budget_year, use_puf_not_cps = ...) -> Dict[Any, TaxCalcParam]: ...
def defaults_all(first_budget_year, use_puf_not_cps = ...) -> Dict[Any, TaxCalcParam]: ...
def nested_form_parameters(budget_year = ..., use_puf_not_cps = ..., defaults = ...) -> List[Dict[Any, List[Dict[Any, Union[TaxCalcParam, dict, List[Dict[Any, TaxCalcParam]]]]]]]: ...
def parse_sub_category(field_section, budget_year, use_puf_not_cps = ...) -> list: ...
def parse_top_level(ordered_dict) -> List[Dict[Any, List[Dict[Any, dict]]]]: ...
