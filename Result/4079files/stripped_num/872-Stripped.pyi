# (generated with --quick)

from typing import Any, Tuple

importlib: module
json: module
logging: module
pika: Any
timezone: Any
uuid: module

class BaseMessageSerializer(object):
    __doc__: str
    content_type: str
    message: Any
    message_type: str
    task_get_attempts: int
    type_header: str
    def __init__(self, message) -> None: ...
    def body(self) -> str: ...
    @classmethod
    def get_task(cls, properties, body) -> Any: ...
    def properties(self) -> dict: ...
    def publish(self, connection, channel) -> None: ...
    def publish_kwargs(self) -> dict: ...
    @classmethod
    def serialize_arguments(cls, body) -> Tuple[Any, Any]: ...

class DefaultMessageSerializer(BaseMessageSerializer):
    message: Any
    message_type: str
    type_header: str

class Message(object):
    __doc__: str
    connection_channel: Tuple[Any, Any]
    exchange: Any
    formatter: DefaultMessageSerializer
    priority: Any
    queue: Any
    routing_key: Any
    task: Any
    task_args: Any
    task_kwargs: Any
    uuid: str
    virtual_host: Any
    def __init__(self, task, virtual_host = ..., queue = ..., routing_key = ..., exchange = ..., priority = ..., task_args = ..., task_kwargs = ...) -> None: ...
    def publish(self, pika_log_level = ...) -> Any: ...

class VirtualHost(object):
    __doc__: str
    blocking_connection: Any
    host: Any
    name: Any
    password: Any
    port: Any
    secure: Any
    username: Any
    def __init__(self, url = ..., host = ..., name = ..., port = ..., username = ..., password = ..., secure = ...) -> None: ...
