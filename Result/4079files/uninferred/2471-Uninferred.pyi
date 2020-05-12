from ..launch_context import LaunchContext as LaunchContext
from ..some_substitutions_type import SomeSubstitutionsType as SomeSubstitutionsType
from ..substitution import Substitution
from typing import Any, Iterable, List, Optional, Text

class EnvironmentVariable(Substitution):
    __name: Any = ...
    __default_value: Any = ...
    def __init__(self, name: SomeSubstitutionsType, *, default_value: Optional[SomeSubstitutionsType]=...) -> None: ...
    @classmethod
    def parse(cls: Any, data: Iterable[SomeSubstitutionsType]) -> Any: ...
    @property
    def name(self) -> List[Substitution]: ...
    @property
    def default_value(self) -> List[Substitution]: ...
    def describe(self) -> Text: ...
    def perform(self, context: LaunchContext) -> Text: ...
