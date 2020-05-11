# (generated with --quick)

from typing import Dict

class ClassBase(type):
    @classmethod
    def __prepare__(mcls, name, bases) -> Dict[str, str]: ...

def populate_dict_from_name(dct, cls_name) -> None: ...
