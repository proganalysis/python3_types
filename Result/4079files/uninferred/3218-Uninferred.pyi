from typing import Any

class _C:
    x: Any = ...
    def __init__(self, x: Any) -> None: ...

dis_c_instance_method: Any
dis_c_instance_method_bytes: str

def _f(a: Any): ...

dis_f: Any
dis_f_co_code: str

def bug708901() -> None: ...

dis_bug708901: Any

def bug1333982(x: Any = ...) -> None: ...

dis_bug1333982: Any
_BIG_LINENO_FORMAT: str
dis_module_expected_results: str
expr_str: str
dis_expr_str: str
simple_stmt_str: str
dis_simple_stmt_str: str
compound_stmt_str: str
dis_compound_stmt_str: str
