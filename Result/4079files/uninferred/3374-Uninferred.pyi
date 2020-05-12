from typing import Any
from whither.bridge import UrlRequestInterceptor as Interceptor

class UrlRequestInterceptor(Interceptor):
    def intercept_request(self, info: Any) -> None: ...
