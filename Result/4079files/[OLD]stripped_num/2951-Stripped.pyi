# (generated with --quick)

from typing import Any, Dict, List, Tuple, Type, Union

AbstractEmailForm: Any
AbstractFormSubmission: Any
BASE_BLOCKS: Any
BaseSetting: Any
COLUMNS_BLOCKS: Any
ContributionBlock: Any
DayBlock: Any
DjangoJSONEncoder: Any
EmailInput: Any
FULL_WIDTH_BLOCKS: Any
FieldPanel: Any
FooterSettings: Any
HeadingAbstractFormField: Any
HeadingFormBuilder: Any
HeadingWidget: Any
ImageChooserPanel: Any
InlinePanel: Any
KeynoteBlock: Any
MultiFieldPanel: Any
Page: Any
ParentalKey: Any
PosterContributionBlock: Any
RichTextField: Any
RichTextFieldPanel: Any
SnippetChooserPanel: Any
StreamField: Any
StreamFieldPanel: Any
TIMELINE_ITEM_PLENARY: str
TIMELINE_ITEM_POSTER: str
TIMELINE_ITEM_SPECIAL: str
TIMELINE_ITEM_TYPES: List[Tuple[str, str]]
TIMELINE_ITEM_WORKSHOP: str
TimelineSnippet: Any
json: module
models: Any
register_setting: Any
render: Any
send_mail: Any
slugify: Any

class AbstractOverviewPage(Any):
    Meta: type
    content_panels: Any
    intro: Any
    parent_page_types: List[str]

class CustomFormSubmission(Any):
    identifier: Any
    def get_data(self) -> Any: ...

class FormField(Any):
    page: Any

class FormPage(Any):
    button_name: Any
    confirmation_email_subject: Any
    confirmation_email_text: Any
    confirmation_text: Any
    content: Any
    content_panels: Any
    form_builder: Any
    form_title: Any
    intro: Any
    landing_page_template: str
    send_confirmation_email: Any
    subpage_types: List[nothing]
    timeline_snippet: Any
    def get_context(self, request, *args, **kwargs) -> Any: ...
    def get_data_fields(self) -> list: ...
    def get_submission_class(self) -> Type[CustomFormSubmission]: ...
    def process_form_submission(self, form) -> None: ...
    def serve(self, request, *args, **kwargs) -> Any: ...

class GenericPage(Any):
    content: Any
    content_panels: Any
    template: str

class HomePage(Any):
    content: Any
    content_panels: Any
    landing_page_template: str
    parent_page_types: List[str]

class PlenaryItemPage(ProgrammeItemPage):
    content: Any
    content_panels: Any
    def get_keynotes(self) -> List[Dict[str, Any]]: ...

class PlenaryOverviewPage(AbstractOverviewPage):
    subpage_types: List[str]
    template: str
    def get_context(self, request, *args, **kwargs) -> Any: ...

class PosterItemPage(ProgrammeItemPage):
    content: Any
    content_panels: Any

class PosterOverviewPage(AbstractOverviewPage):
    subpage_types: List[str]
    template: str
    def get_context(self, request, *args, **kwargs) -> Any: ...

class ProgramOverviewPage(Any):
    content: Any
    content_panels: Any
    intro: Any
    parent_page_types: List[str]
    subpage_types: List[str]
    def get_context(self, request, *args, **kwargs) -> Any: ...
    def get_sidebar_menu(self, active_menu_item = ...) -> List[Dict[str, Any]]: ...

class ProgrammeItemPage(Any):
    Meta: type
    content_panels: Any
    date_time: Any
    description: Any
    icon: Any
    parent_page_types: List[str]
    room: Any

class SidebarPage(Any):
    content: Any
    content_panels: Any
    intro: Any
    parent_page_types: List[Union[str, Type[HomePage]]]
    def get_context(self, request, *args, **kwargs) -> Any: ...

class WorkshopChallengePage(Any):
    challenge_icon: Any
    content_panels: Any
    description: Any
    parent_page_types: List[str]
    subpage_types: List[str]
    workshop_icon: Any

class WorkshopItemPage(ProgrammeItemPage):
    content: Any
    content_panels: Any
    convenor_institute: Any
    convenor_name: Any

class WorkshopOverviewPage(AbstractOverviewPage):
    subpage_types: List[str]
    template: str
    def get_context(self, request, *args, **kwargs) -> Any: ...
    def get_workshops(self, date_time) -> List[Dict[str, Any]]: ...
