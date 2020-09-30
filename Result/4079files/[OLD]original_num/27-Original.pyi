# (generated with --quick)

from typing import Any

JsonResponse: Any
SearchForm: Any
SearchQuerySet: Any
SearchView: Any

class ProjectSearchView(Any):
    form_class: Any
    paginate_by: int
    queryset: Any
    template_name: str
    def get_context_data(self, **kwargs) -> Any: ...

def autocomplete(request) -> Any: ...
