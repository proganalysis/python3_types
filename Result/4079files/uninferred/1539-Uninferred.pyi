from src.pages import MyFlatPages as MyFlatPages
from typing import Any, Dict

root_folder_path: Any
pdf_folder_path: Any
PDF_CONFIG: Any
PDF_TOC_CONFIG: Any

def generate_pdf(build_mode: bool, pages: Any, toc: Any) -> Any: ...
def get_pdf_content(build_mode: bool, pages: MyFlatPages, toc: Dict) -> str: ...
