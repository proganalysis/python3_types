# (generated with --quick)

from typing import Any, NoReturn

INT_VALUE: int
Injector: Any
LENGTH: int
Module: Any
STR_VALUE: str
basic_injected_function: Any
defaulted_injected_function: Any
injector: Any
modules: Any
parametrized_injected_function: Any
provide_string: Any
provider: Any
pytest: Any
test_missing_dependency: Any
test_missing_dependency_provided: Any

class AltModuleSync(Any):
    provide_bool: Any

class ModuleSync(Any):
    provide_int: Any

def assert_wrapped(wrapped_func) -> None: ...
def test_basic(basic_injected_function) -> None: ...
def test_basic_manual(basic_injected_function) -> None: ...
def test_classmethod(injector) -> None: ...
def test_inject_param(parametrized_injected_function) -> None: ...
def test_instancemethod(injector) -> None: ...
def test_module_dependencies(injector) -> None: ...
def test_module_unloading(injector) -> NoReturn: ...
def test_provided_defaults(defaulted_injected_function) -> None: ...
def test_staticmethod(injector) -> None: ...
