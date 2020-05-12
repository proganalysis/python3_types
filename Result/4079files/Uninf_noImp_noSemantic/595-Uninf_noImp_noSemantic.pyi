from typing import Any, Dict, Tuple

class BaseAnalytics:
    _instances: Dict[Tuple[Any, ...], BaseAnalytics] = ...
    async def async_init(self) -> None: ...
    async def page_view(self, url: str, title: str, user_id: str, user_lang: str=...) -> None: ...
    def hash_user_id(self, user_id: str) -> str: ...
    @classmethod
    async def instance(cls: Any, *args: Any) -> BaseAnalytics: ...

def new_task(func: Any): ...
async def providers() -> None: ...
