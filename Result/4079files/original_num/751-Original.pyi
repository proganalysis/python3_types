# (generated with --quick)

import typing
from typing import Any, Type

Counter: Type[typing.Counter]
Repo2Base: Any
SIMPLE_IDENTIFIER: Any
c2v: Repo2IdCounter
repo: str

class Repo2IdCounter(Any):
    MODEL_CLASS: Type[Repo2IdModel]
    __doc__: str
    def collect_id_cnt(self, root, id_cnt) -> None: ...
    def convert_uasts(self, file_uast_generator) -> None: ...

class Repo2IdModel:
    NAME: str
