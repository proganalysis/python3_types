# (generated with --quick)

import flask.ctx
from typing import Any, Type

Application: Any
Community: Any
CommunityIdColumn: Any
Entity: Any
Folder: Any
MEMBER: Any
READER: Any
RequestContext: Type[flask.ctx.RequestContext]
SQLAlchemy: Any
Session: Any
User: Any
community: Any
community_content: Any
fixture: Any
login: Any
mock: module
orm: Any
pytest: Any
sa: Any
signals: Any
views: Any

def test_auto_slug(community) -> None: ...
def test_can_recreate_with_same_name(community, db) -> None: ...
def test_community_content_decorator(community, db) -> None: ...
def test_community_indexed(app, db, req_ctx) -> None: ...
def test_default_url(app, community) -> None: ...
def test_default_view_kw() -> None: ...
def test_default_view_kw_with_hit(app, db, community, req_ctx) -> None: ...
def test_folder_roles(community, db, app) -> None: ...
def test_instanciation(db) -> None: ...
def test_membership(community, db) -> None: ...
def test_rename(community) -> None: ...
