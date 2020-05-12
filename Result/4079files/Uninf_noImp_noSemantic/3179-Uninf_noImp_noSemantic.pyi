from namecheapapi.api.session import Session
from typing import Any

class UserAPI:
    session: Any = ...
    def __init__(self, session: Session) -> None: ...
    def get_pricing(self) -> None: ...
    def get_balances(self) -> None: ...
    def change_password(self) -> None: ...
    def update(self) -> None: ...
    def create_add_funds_request(self) -> None: ...
    def get_add_funds_status(self) -> None: ...
    def create(self) -> None: ...
    def login(self) -> None: ...
    def reset_password(self) -> None: ...
    def create_address(self) -> None: ...
    def delete_address(self) -> None: ...
    def get_address_info(self) -> None: ...
    def get_address_list(self) -> None: ...
    def set_default_address(self) -> None: ...
    def update_address(self) -> None: ...
