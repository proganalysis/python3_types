# (generated with --quick)

import flask.wrappers
import forms
from typing import Any, Dict, Iterable, NoReturn, Type, TypeVar, Union
import werkzeug.wrappers

Admiral: Any
BaseModelForm: Any
ConfirmRegisterForm: Any
Form: Any
Mail: Any
Migrate: Any
ModelForm: Type[forms.ModelForm]
MyRegisterForm: Type[forms.MyRegisterForm]
Role: Any
SQLAlchemyUserDatastore: Any
Security: Any
User: Any
admin: Any
current_user: Any
datetime: module
db: Any
fields: Any
g: Any
logger: logging.Logger
logging: module
model_form_factory: Any
modules: Dict[str, Any]
request: flask.wrappers.Request
user_logged_in: Any
validators: Any

_RC = TypeVar('_RC', bound=werkzeug.wrappers.Response)

def abort(status: Union[int, werkzeug.wrappers.Response], *args, **kwargs) -> NoReturn: ...
def generate_api_token() -> str: ...
def init(app) -> None: ...
@overload
def redirect(location, code: int = ..., Response: None = ...) -> werkzeug.wrappers.Response: ...
@overload
def redirect(location, code: int = ..., Response: Type[_RC] = ...) -> _RC: ...
def render_template(template_name_or_list: Union[str, Iterable[str]], **context) -> str: ...
def send_from_directory(directory, filename, **options) -> Any: ...
