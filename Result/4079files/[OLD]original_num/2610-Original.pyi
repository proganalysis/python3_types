# (generated with --quick)

import misc.deploy
from typing import Any, Type

Application: Type[misc.deploy.Application]
DatabaseError: Any
components: module
exceptions: Any
microservice: Microservice
os: module
read_migrations: Any

class Microservice(misc.deploy.Application):
    @staticmethod
    def _do_migrations() -> None: ...
