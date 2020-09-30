# (generated with --quick)

from typing import Any

SqlAlchemyBase: Any
blue_yellow_app: Any
sqlalchemy: Any

class DbSessionFactory:
    factory: Any
    @staticmethod
    def create_session() -> Any: ...
    @staticmethod
    def global_init(db_file) -> None: ...
