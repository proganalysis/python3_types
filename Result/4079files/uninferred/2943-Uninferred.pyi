from django.http import HttpResponse
from typing import Any, Optional

REDIRECT_HEADER_KEY: str

class HttpResponseJavascriptRedirect(HttpResponse):
    def __init__(self, redirect_to: Optional[Any] = ..., *args: Any, **kwargs: Any) -> None: ...
