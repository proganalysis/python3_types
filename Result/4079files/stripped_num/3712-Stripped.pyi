# (generated with --quick)

from typing import Any
import unittest.case

APIRequestError: Any
ContactModel: Any
DomainInfo: Any
DomainProcessingError: Any
NameSilo: Any
mock: module
mocked_data: Any
mocked_single_contact: Any
unittest: module

class NameSiloTestCase(unittest.case.TestCase):
    ns: Any
    test_account_balance: Any
    test_add_contact: Any
    test_add_domain_privacy: Any
    test_add_funds: Any
    test_auto_renew_domain: Any
    test_change_domain_nameservers: Any
    test_contacts_lists: Any
    test_contacts_lists_only_one_contact: Any
    test_delete_contact: Any
    test_domain_check_available: Any
    test_domain_check_not_available: Any
    test_domain_price: Any
    test_domain_registration: Any
    test_domain_registration_fail: Any
    test_domain_renewal: Any
    test_get_content_xml: Any
    test_get_content_xml_exception: Any
    test_get_domain_info: Any
    test_list_domains: Any
    test_lock_domain: Any
    test_process_data: Any
    test_remove_auto_renew_domain: Any
    test_remove_domain_privacy: Any
    test_unlock_domain: Any
    test_update_contact: Any
    def test_check_error_code(self) -> None: ...
    def test_check_error_code_exception(self) -> None: ...
    def test_production_api_url(self) -> None: ...
    def test_sandbox_api_url(self) -> None: ...
