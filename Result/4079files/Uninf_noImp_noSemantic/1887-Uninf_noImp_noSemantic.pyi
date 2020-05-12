from aiogithub import objects
from aiogithub.objects.response import BaseResponseObject
from typing import Any, Optional

class Review(BaseResponseObject):
    _url: str = ...
    _default_urls: Any = ...
    @staticmethod
    def _get_key_mappings(): ...
    async def get_pull_request(self) -> objects.PullRequest: ...
    @property
    def id(self) -> Optional[int]: ...
    @property
    def user(self) -> objects.PartialUser: ...
    @property
    def body(self) -> Optional[str]: ...
    @property
    def commit_id(self) -> Optional[str]: ...
    @property
    def state(self) -> Optional[str]: ...
    @property
    def html_url(self) -> Optional[str]: ...
    @property
    def _links(self) -> dict: ...
