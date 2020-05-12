# (generated with --quick)

from typing import Any, List, Type

ChipScan: Any
ChipScanFilter: Any
CreateWithInlinesView: Any
CustomBaseInlineFormSet: Any
Http404: Any
HttpResponseRedirect: Any
InlineFormSet: Any
LapResult: Any
ManageChipScanTable: Any
ManageLapResultForm: Any
ManageResultTable: Any
ManagerPermissionMixin: Any
NamedFormsetsMixin: Any
Q: Any
RequestFormKwargsMixin: Any
Result: Any
ResultForm: Any
ResultListSearchForm: Any
SetCompetitionContextMixin: Any
SingleTableViewWithRequest: Any
TemplateView: Any
UpdateView: Any
UpdateWithInlinesView: Any
UrlSync: Any
UrlSyncForm: Any
UrlSyncTable: Any
__all__: List[str]
generate_pdfreport: Any
messages: Any
result_process: Any
reverse: Any
slugify: Any

class ManagLapResultInline(Any):
    can_order: bool
    extra: int
    form_class: Any
    formset_class: Any
    model: Any
    def get_extra_form_kwargs(self) -> Any: ...
    def get_formset_kwargs(self) -> Any: ...

class ManageChipScanList(Any, Any):
    filter_class: Any
    model: Any
    table_class: Any
    template_name: str
    def get_queryset(self) -> Any: ...
    def post(self, request, *args, **kwargs) -> Any: ...

class ManageResultCreate(Any, Any, Any, Any, Any):
    form_class: Any
    inlines: List[Type[ManagLapResultInline]]
    inlines_names: List[str]
    model: Any
    pk_url_kwarg: str
    template_name: str
    def get_success_url(self) -> Any: ...

class ManageResultList(Any, Any):
    model: Any
    table_class: Any
    template_name: str
    def get_context_data(self, **kwargs) -> Any: ...
    def get_queryset(self) -> Any: ...

class ManageResultReports(Any, Any, Any):
    template_name: str
    def post(self, request, *args, **kwargs) -> Any: ...

class ManageResultUpdate(Any, Any, Any, Any, Any):
    form_class: Any
    inlines: List[Type[ManagLapResultInline]]
    inlines_names: List[str]
    model: Any
    pk_url_kwarg: str
    template_name: str
    def get_success_url(self) -> Any: ...

class ManageUrlSyncList(Any, Any):
    model: Any
    table_class: Any
    template_name: str

class ManageUrlSyncUpdate(Any, Any, Any, Any):
    form_class: Any
    model: Any
    pk_url_kwarg: str
    template_name: str
    def get_success_url(self) -> Any: ...
