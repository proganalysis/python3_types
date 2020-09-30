# (generated with --quick)

from typing import Any
import unittest.case

DATABASE_DIR_PATH: str
DB_NAME: str
DB_URL: Any
HOST: str
PASSWORD: str
PORT: str
URL: Any
USER: str
create_engine: Any
os: module
sqlalchemy: Any
subprocess: module
unittest: module

class TestDBSchemaMigration(unittest.case.TestCase):
    def _run_alembic(self, alembic_cmd) -> bytes: ...
    def test_db_schema_migration_script(self) -> None: ...
