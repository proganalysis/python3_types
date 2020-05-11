# (generated with --quick)

from typing import Any

QUERY: str
psycopg2: Any
pytest: Any
test_postgres_terminate_connection: Any
test_postgresql_proc: Any

def test_main_postgres(postgresql) -> None: ...
def test_rand_postgres_port(postgresql_rand) -> None: ...
def test_two_postgreses(postgresql, postgresql2) -> None: ...
