from flask_admin import AdminIndexView
from typing import Any, Optional

class MyAdminIndexView(AdminIndexView):
    def __init__(self, endpoint: Optional[Any] = ..., url: Optional[Any] = ...) -> None: ...
    def index(self): ...

admin: Any
