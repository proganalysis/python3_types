from typing import Any

auth_cookie_name: str

def set_auth(request: Any, user_id: Any): ...
def __hash_text(text: Any): ...
def __add_cookie_callback(_: Any, response: Any, name: Any, value: Any) -> None: ...
def get_user_id_via_auth_cookie(request: Any): ...
def logout(request: Any): ...
def __delete_cookie_callback(response: Any, name: Any) -> None: ...
