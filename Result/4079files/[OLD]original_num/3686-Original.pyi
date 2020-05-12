# (generated with --quick)

import enum
import notifier.model
import notifier.zendesk
import tests
from typing import Any, Dict, Iterable, Type, Union

AsyncContext: Type[tests.AsyncContext]
AsyncTestCase: Type[tests.AsyncTestCase]
DiffError: Type[notifier.model.`namedtuple-DiffError-url_errors-md_error-section_link`]
DynamicContentItem: Type[notifier.model.`namedtuple-DynamicContentItem-key-wti_id-zendesk_item`]
Enum: Type[enum.Enum]
GoogleLanguage: Type[notifier.model.`namedtuple-GoogleLanguage-language-name`]
GoogleTranslation: Type[notifier.model.`namedtuple-GoogleTranslation-translatedText-model-detectedSourceLanguage`]
TranslationError: Type[notifier.model.TranslationError]
UnknownResponse: Type[notifier.model.UnknownResponse]
UnsupportedLocale: Type[notifier.model.UnsupportedLocale]
WtiContentTypes: Type[notifier.model.WtiContentTypes]
WtiError: Type[notifier.model.WtiError]
WtiProject: Type[notifier.model.`namedtuple-WtiProject-id-name-master_locale-filename-content_type`]
WtiString: Type[notifier.model.`namedtuple-WtiString-id-locale-text-status-updated_at-plural`]
WtiStringStatus: Type[notifier.model.WtiStringStatus]
WtiTranslationStatus: Type[notifier.model.WtiTranslationStatus]
WtiUser: Type[notifier.model.`namedtuple-WtiUser-id-email-role`]
WtiUserRoles: Type[notifier.model.WtiUserRoles]
ZendeskItem: Type[notifier.model.`namedtuple-ZendeskItem-id-name-text-variants`]
`namedtuple-DiffError-url_errors-md_error-section_link`: Type[notifier.model.`namedtuple-DiffError-url_errors-md_error-section_link`]
`namedtuple-DynamicContentItem-key-wti_id-zendesk_item`: Type[notifier.model.`namedtuple-DynamicContentItem-key-wti_id-zendesk_item`]
`namedtuple-GoogleLanguage-language-name`: Type[notifier.model.`namedtuple-GoogleLanguage-language-name`]
`namedtuple-GoogleTranslation-translatedText-model-detectedSourceLanguage`: Type[notifier.model.`namedtuple-GoogleTranslation-translatedText-model-detectedSourceLanguage`]
`namedtuple-WtiProject-id-name-master_locale-filename-content_type`: Type[notifier.model.`namedtuple-WtiProject-id-name-master_locale-filename-content_type`]
`namedtuple-WtiString-id-locale-text-status-updated_at-plural`: Type[notifier.model.`namedtuple-WtiString-id-locale-text-status-updated_at-plural`]
`namedtuple-WtiUser-id-email-role`: Type[notifier.model.`namedtuple-WtiUser-id-email-role`]
`namedtuple-ZendeskItem-id-name-text-variants`: Type[notifier.model.`namedtuple-ZendeskItem-id-name-text-variants`]
zendesk: module

class TestZendesk(tests.AsyncTestCase):
    client: notifier.zendesk.ZendeskDynamicContent
    locales: Dict[str, int]
    def test_item_variants(self) -> None: ...
    def test_items(self) -> None: ...
    def test_items_pagination(self) -> None: ...
    def test_update(self) -> None: ...

def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def read_fixture(filename, mode = ..., decoder = ...) -> Any: ...
