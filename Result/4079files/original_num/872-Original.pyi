# (generated with --quick)

from typing import Any, Callable, Optional, Tuple, Union

importlib: module
json: module
logging: module
pika: Any
timezone: Any
uuid: module

class BaseMessageSerializer(object):
    __doc__: str
    content_type: str
    message: Message
    message_type: str
    task_get_attempts: int
    type_header: str
    def __init__(self, message: Message) -> None: ...
    def body(self) -> str: ...
    @classmethod
    def get_task(cls, properties, body: bytes) -> Callable: ...
    def properties(self) -> dict: ...
    def publish(self, connection, channel) -> None: ...
    def publish_kwargs(self) -> dict: ...
    @classmethod
    def serialize_arguments(cls, body: str) -> Tuple[tuple, dict]: ...

class DefaultMessageSerializer(BaseMessageSerializer):
    message: Message
    message_type: str
    type_header: str

class Message(object):
    __doc__: str
    connection_channel: Tuple[Any, Any]
    exchange: str
    formatter: DefaultMessageSerializer
    priority: int
    queue: str
    routing_key: Any
    task: str
    task_args: tuple
    task_kwargs: Any
    uuid: str
    virtual_host: Any
    def __init__(self, task: str, virtual_host: Optional[VirtualHost] = ..., queue: str = ..., routing_key: Optional[str] = ..., exchange: str = ..., priority: int = ..., task_args: tuple = ..., task_kwargs: Optional[Union[dict, str]] = ...) -> None: ...
    def publish(self, pika_log_level: int = ...) -> Any: ...

class VirtualHost(object):
    __doc__: str
    blocking_connection: Any
    host: Any
    name: Any
    password: Any
    port: int
    secure: bool
    username: Any
    def __init__(self, url: Optional[str] = ..., host: str = ..., name: str = ..., port: int = ..., username: str = ..., password: str = ..., secure: bool = ...) -> None: ...
