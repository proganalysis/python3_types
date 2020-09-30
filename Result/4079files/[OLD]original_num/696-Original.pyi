# (generated with --quick)

from typing import Any, Callable, Coroutine, List, Pattern, Tuple

Image: module
ImageDraw: module
asyncio: module
cat_body: Any
cat_head: Any
cat_tail: Any
db: Any
discord: Any
faces: Tuple[str, str]
io: module
message_handlers: List[Tuple[Pattern[str], bool, Any]]
random: module
re: module
response_names: Tuple[str, ...]

class ChannelResponses(Any):
    __tablename__: str
    id: Any
    name: str

class GuildResponses(Any):
    __tablename__: str
    id: Any
    name: str

class UserResponses(Any):
    __tablename__: str
    id: Any
    name: str

def brutal_savage_rekt(ctx, match) -> Coroutine[Any, Any, None]: ...
def dad_jokes(ctx, match) -> Coroutine[Any, Any, None]: ...
def hat_hat(ctx, match) -> Coroutine[Any, Any, None]: ...
def load(category, name) -> Any: ...
def longcat(ctx, match) -> Coroutine[Any, Any, None]: ...
def message_listener(ctx) -> Coroutine[Any, Any, None]: ...
def on_message(pattern, *flags, start_only = ...) -> Callable[[Any], Any]: ...
def pointing_faces(ctx, match) -> Coroutine[Any, Any, None]: ...
def setup(bot) -> None: ...
