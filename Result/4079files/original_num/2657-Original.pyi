# (generated with --quick)

import redis.client
from typing import Any

config: Any
psycopg2: Any
raven: Any
redis: module
riemann_client: Any

def get_psql(dbname = ...) -> Any: ...
def get_raven() -> Any: ...
def get_redis() -> redis.client.Redis: ...
def get_riemann() -> Any: ...
