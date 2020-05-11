# (generated with --quick)

from typing import Any

logbook: Any
mailchimp: Any

class MailingListService:
    _MailingListService__log: Any
    mailchimp_api: Any
    mailchimp_list_id: Any
    @staticmethod
    def add_subscriber(email) -> bool: ...
    @staticmethod
    def get_is_initialized() -> Any: ...
    @staticmethod
    def global_init(api_key, list_id) -> None: ...
