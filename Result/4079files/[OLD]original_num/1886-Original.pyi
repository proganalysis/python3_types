# (generated with --quick)

import argparse
import redis.filter
from typing import Any, Coroutine, List, Mapping, Optional, Tuple, Type

ArgumentDefaultsHelpFormatter: Type[argparse.ArgumentDefaultsHelpFormatter]
AuthenticationCredentials: Any
BackendInterface: Any
BaseSession: Any
FilterSet: Type[redis.filter.FilterSet]
IMAPConfig: Any
InvalidAuth: Any
LoginProtocol: Any
MailboxConflict: Any
MailboxSet: Any
Message: Any
Namespace: Type[argparse.Namespace]
Redis: Any
__all__: List[str]
create_redis: Any
json: module
ldap_context: Any
uuid: module

class Config(Any):
    __doc__: str
    _address: str
    _prefix: str
    _select: Any
    _users_hash: Any
    _users_json: bool
    _users_key: str
    address: str
    namespace_hash: str
    prefix: str
    select: Optional[int]
    users_hash: Optional[str]
    users_json: bool
    users_key: str
    def __init__(self, args: argparse.Namespace, *, address: str, select: Optional[int], prefix: str, users_hash: Optional[str], users_key: str, users_json: bool, **extra) -> None: ...
    @classmethod
    def parse_args(cls, args: argparse.Namespace) -> Mapping[str, Any]: ...

class RedisBackend(Any):
    __doc__: str
    _config: Any
    _login: Any
    config: Any
    login: Any
    def __init__(self, login, config) -> None: ...
    @classmethod
    def add_subparser(cls, name: str, subparsers) -> None: ...
    @classmethod
    def init(cls, args: argparse.Namespace) -> Coroutine[Any, Any, Tuple[RedisBackend, Config]]: ...

class Session(Any):
    __doc__: str
    _config: Config
    _filter_set: redis.filter.FilterSet
    _mailbox_set: Any
    _redis: Any
    config: Any
    filter_set: redis.filter.FilterSet
    mailbox_set: Any
    resource: str
    def __init__(self, redis, owner: str, config: Config, mailbox_set, filter_set: redis.filter.FilterSet) -> None: ...
    @classmethod
    def _check_user(cls, redis, config: Config, credentials) -> Coroutine[Any, Any, bytes]: ...
    @classmethod
    def _get_password(cls, redis, config: Config, name: str) -> Coroutine[Any, Any, Tuple[str, bytes]]: ...
    def cleanup(self) -> Coroutine[Any, Any, None]: ...
    @classmethod
    def login(cls, credentials, config: Config) -> Coroutine[Any, Any, Session]: ...
