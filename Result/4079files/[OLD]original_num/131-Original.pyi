# (generated with --quick)

from typing import Any, Tuple, Type

BaseQuery: Any
Channel: Any
ChannelID: Any
ItemID: Any
ReprBuilder: Any
User: Any
UserID: Any
association_proxy: Any
datetime: Type[datetime.datetime]
db: Any
generate_uuid: Any
load_template: Any

class CurrentVersionAssociation(Any):
    __tablename__: str
    item: Any
    item_id: Any
    version: Any
    version_id: Any
    def __init__(self, item: Item, version: ItemVersion) -> None: ...

class Item(Any):
    __doc__: str
    __table_args__: Tuple[Any]
    __tablename__: str
    channel: Any
    channel_id: Any
    created_at: Any
    current_version: Any
    id: Any
    published: bool
    published_at: Any
    query_class: Type[ItemQuery]
    slug: Any
    title: str
    def __init__(self, channel_id, slug: str) -> None: ...
    def __repr__(self) -> str: ...

class ItemQuery(Any):
    def for_channel(self, channel_id) -> Any: ...
    def published(self) -> Any: ...
    def with_current_version(self) -> Any: ...

class ItemVersion(Any):
    __doc__: str
    __tablename__: str
    body: Any
    created_at: Any
    creator: Any
    creator_id: Any
    id: Any
    image_url_path: Any
    is_current: bool
    item: Any
    item_id: Any
    query_class: Type[ItemVersionQuery]
    title: Any
    def __init__(self, item: Item, creator_id, title: str, body: str) -> None: ...
    def __repr__(self) -> str: ...
    def render_body(self) -> str: ...

class ItemVersionQuery(Any):
    def for_item(self, item_id) -> Any: ...
