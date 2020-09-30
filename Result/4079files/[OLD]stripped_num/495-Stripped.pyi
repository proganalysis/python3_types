# (generated with --quick)

from typing import Any, Union

datafiles: Any
factory: ObjectsFactory
ob1: Union[AnObject, bool]
objectTypes: Any
path: module
yaml: module

class AnObject:
    typ: Any
    def __init__(self, typ) -> None: ...

class ObjectsFactory:
    objectsFilename: Any
    objetcsPrototypes: Any
    def __init__(self) -> None: ...
    def createObject(self, name) -> Union[AnObject, bool]: ...
    def load(self) -> None: ...
