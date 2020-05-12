from core.framework.common import *
from sqlalchemy import create_engine as create_engine
from typing import Any, Optional

def init_pg(user: Any, password: Any, host: Any, port: Any, db: Any): ...

Base: Any
__db_engine: Any
Session: Any
__db_session: Any
__db_pool: Any
__async_job_id: int
__async_jobs: Any

def __execute_async(async_job_id: Any, query: Any): ...
def __execute_callback(result: Any) -> None: ...
def get_or_create(session: Any, model: Any, defaults: Optional[Any] = ..., **kwargs: Any): ...
def check_session(obj: Any) -> None: ...
def generic_save(obj: Any) -> None: ...
def generic_count(obj: Any): ...
def session(): ...
def execute(query: Any): ...
def execute_bw(query: Any, callback: Optional[Any] = ...): ...
async def execute_aio(query: Any): ...
def cancel(async_job_id: Any) -> None: ...
