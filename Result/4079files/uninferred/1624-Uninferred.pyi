from django import forms
from django.views import View
from typing import Any, Optional
from website.views import PlusMemberCheck

User: Any

class ProblemListForm(forms.Form):
    q: Any = ...
    search_by: Any = ...

class ProblemListView(PlusMemberCheck, View):
    def get(self, request: Any): ...

class ProblemGetView(PlusMemberCheck, View):
    def get(self, request: Any, pk: Any): ...

class ProblemAuthForm(forms.Form):
    auth_key: Any = ...

class ProblemAuthView(PlusMemberCheck, View):
    def post(self, request: Any, pk: Any): ...

class ProblemDownloadView(PlusMemberCheck, View):
    def get(self, request: Any, pk: Any): ...

class ProblemRankView(PlusMemberCheck, View):
    def get(self, request: Any, pk: Optional[Any] = ...): ...

class ProblemQuestionView(PlusMemberCheck, View):
    def get(self, request: Any): ...

class ProblemQuestionAskForm(forms.Form):
    question: Any = ...

class ProblemQuestionAskView(PlusMemberCheck, View):
    def post(self, request: Any, pk: Any): ...

class ProblemUserView(PlusMemberCheck, View):
    def get(self, request: Any): ...
