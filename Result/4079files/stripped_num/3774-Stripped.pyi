# (generated with --quick)

from typing import Any

c: Child
p: Parent

class Child(Parent):
    _Child__new_obj_var: Any
    _Parent__class_var: int
    _Parent__obj_var: Any
    __doc__: str
    child_var: Any
    def __init__(self, obj_var, new_ojb_var) -> None: ...

class Parent(object):
    _Parent__class_var: int
    _Parent__obj_var: Any
    __doc__: str
    obj_var: Any
    def __init__(self, obj_var) -> None: ...
    @classmethod
    def get_class_var(cls) -> Any: ...
    @classmethod
    def set_class_var(cls, value) -> None: ...
