from typing import Any

def populate_dict_from_name(dct: Any, cls_name: Any) -> None: ...

class ClassBase(type):
    @classmethod
    def __prepare__(mcls: Any, name: Any, bases: Any): ...
