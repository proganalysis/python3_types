# (generated with --quick)

import argparse
import redis.filter
from typing import Any, Coroutine, Dict, List, Tuple, Type

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
    _address: Any
    _prefix: Any
    _select: Any
    _users_hash: Any
    _users_json: Any
    _users_key: Any
    address: Any
    namespace_hash: str
    prefix: Any
    select: Any
    users_hash: Any
    users_json: Any
    users_key: Any
    def __init__(self, args, *, address, select, prefix, users_hash, users_key, users_json, **extra) -> None: ...
    @classmethod
    def parse_args(cls, args) -> Dict[str, Any]: ...

class RedisBackend(Any):
    __doc__: str
    _config: Any
    _login: Any
    config: Any
    login: Any
    def __init__(self, login, config) -> None: ...
    @classmethod
    def add_subparser(cls, name, subparsers) -> None: ...
    @classmethod
    def init(cls, args) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...

class Session(Any):
    __doc__: str
    _config: Any
    _filter_set: Any
    _mailbox_set: Any
    _redis: Any
    config: Any
    filter_set: Any
    mailbox_set: Any
    resource: str
    def __init__(self, redis, owner, config, mailbox_set, filter_set) -> None: ...
    @classmethod
    def _check_user(cls, redis, config, credentials) -> coroutine: ...
    @classmethod
    def _get_password(cls, redis, config, name) -> Coroutine[Any, Any, Tuple[Any, Any]]: ...
    def cleanup(self) -> Coroutine[Any, Any, None]: ...
    @classmethod
    def login(cls, credentials, config) -> coroutine: ...
