# (generated with --quick)

from typing import Any, Optional

Exceptions: Any
Utils: Any
datetime: module
io: module
json: module
logging: module
requests: module
time: module

class Model:
    _Model__model_image: None
    _Model__online: None
    _Model__status: None
    _response: Any
    autoupdate: Any
    last_update: Optional[datetime.datetime]
    model_image: Any
    online: Any
    status: Any
    username: Any
    def __init__(self, username, autoupdate = ...) -> None: ...
    def update_model_image(self) -> None: ...
    def update_model_status(self) -> None: ...
