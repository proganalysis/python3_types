# (generated with --quick)

import datetime
from typing import Any, Callable, Iterable, Type, TypeVar

AuthReplay: Any
Category: Any
FileResponse: Any
Http404: Any
HttpResponseBadRequest: Any
HttpResponseServerError: Any
IntegrityError: Any
JsonResponse: Any
ObjectDoesNotExist: Any
PlusMemberCheck: Any
ProblemAttachment: Any
ProblemAuthLog: Any
ProblemInstance: Any
ProblemList: Any
ProblemQuestion: Any
Session: Any
User: Any
View: Any
forms: Any
get_problem_list_total_score: Any
get_problem_list_user_info: Any
get_problem_list_user_score: Any
get_user_model: Any
get_user_problem_info: Any
mimetypes: module
os: module
render: Any
timedelta: Type[datetime.timedelta]
urlquote: Any

_S = TypeVar('_S')
_T = TypeVar('_T')

class ProblemAuthForm(Any):
    auth_key: Any

class ProblemAuthView(Any, Any):
    def post(self, request, pk) -> Any: ...

class ProblemDownloadView(Any, Any):
    def get(self, request, pk) -> Any: ...

class ProblemGetView(Any, Any):
    def get(self, request, pk) -> Any: ...

class ProblemListForm(Any):
    q: Any
    search_by: Any

class ProblemListView(Any, Any):
    def get(self, request) -> Any: ...

class ProblemQuestionAskForm(Any):
    question: Any

class ProblemQuestionAskView(Any, Any):
    def post(self, request, pk) -> Any: ...

class ProblemQuestionView(Any, Any):
    def get(self, request) -> Any: ...

class ProblemRankView(Any, Any):
    def get(self, request, pk = ...) -> Any: ...

class ProblemUserView(Any, Any):
    def get(self, request) -> Any: ...

@overload
def reduce(function: Callable[[_T, _S], _T], sequence: Iterable[_S], initial: _T) -> _T: ...
@overload
def reduce(function: Callable[[_T, _T], _T], sequence: Iterable[_T]) -> _T: ...
