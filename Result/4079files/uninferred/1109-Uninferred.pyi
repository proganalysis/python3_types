import asyncio
import gettext
from typing import Any
from wpull.pipeline.app import AppSession
from wpull.pipeline.pipeline import ItemTask

_logger: Any
_ = gettext.gettext

class URLFiltersSetupTask(ItemTask[AppSession]):
    @asyncio.coroutine
    def process(self, session: AppSession) -> Any: ...
    @classmethod
    def _build_url_rewriter(cls: Any, session: AppSession) -> Any: ...
    @classmethod
    def _build_url_filters(cls: Any, session: AppSession) -> Any: ...

class URLFiltersPostURLImportSetupTask(ItemTask[AppSession]):
    @asyncio.coroutine
    def process(self, session: AppSession) -> Any: ...
