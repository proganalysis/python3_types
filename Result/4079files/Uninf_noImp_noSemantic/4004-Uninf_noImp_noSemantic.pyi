from .template_engine import TemplateEngine
from .tr_support import MultiLangTranslator
from typing import Any

def erro_page_detect_request_locale(tr: MultiLangTranslator) -> str: ...
def error_page_create_template_engine(title: str, mode: str) -> TemplateEngine: ...
def page_404(status: Any, message: Any, traceback: Any, version: Any): ...
def page_500(status: Any, message: Any, traceback: Any, version: Any): ...
