# (generated with --quick)

from typing import Any, Callable, Iterable, Iterator, Optional, TypeVar

collections: module
docker: Any
itertools: module
kubernetes: Any
once_per_task: Any
six: module
utils: Any

_T = TypeVar('_T')

class DjangoContainer(Any, DjangoMixin): ...

class DjangoKubernetes(Any, DjangoMixin): ...

class DjangoMixin(Any):
    __doc__: str
    migrate: Any
    migrate_back: Any
    @staticmethod
    def _get_parent_migration(migration, migrations) -> Any: ...
    @staticmethod
    def _migrate(image, options) -> None: ...
    def get_revert_migrations(self, current_migrations, backup_migrations) -> dict_values: ...

class DjangoService(Any, DjangoMixin): ...

class DjangoStack(Any, DjangoMixin): ...

class Migration(str):
    app: str
    name: str
    def __init__(self, *args, **kwargs) -> None: ...

def filter(function: Optional[Callable[[_T], Any]], iterable: Iterable[_T]) -> Iterator[_T]: ...
@overload
def map(function, *sequences: Iterable[nothing]) -> Iterator[nothing]: ...
@overload
def map(function: Callable[..., _T], *sequences: Iterable) -> Iterator[_T]: ...
