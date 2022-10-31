# (generated with --quick)

from typing import Any, Callable, Optional, Pattern, Type, Union

DOUBLE_NEWLINE_RE: Pattern[str]
HEADER_TITLE_RE: Pattern[str]
LINK_RE: Pattern[str]
SRC_RE: Pattern[str]
TITLE_RE: Pattern[str]
datetime: Type[datetime.datetime]
markdown: Any
os: module
re: module

def DEFAULT_ON_CREATE(_) -> None: ...
def compile_markdown(file_path: str) -> str: ...
def compile_plaintext(file_path: str) -> str: ...
def compile_source_file(source_file_path: str, header_content: str, footer_content: str) -> str: ...
def compile_wiki(source_path: str, dest_path: str, on_create: Callable[[str], None] = ...) -> None: ...
def copy(src: Union[str, _PathLike[str]], dst: Union[str, _PathLike[str]], *, follow_symlinks: bool = ...) -> Any: ...
def depth_from(root: str, path: str) -> int: ...
def extract_title(content: str) -> Optional[str]: ...
def generate_toc(header_content, articles) -> str: ...
def relativize_links(content: str, depth: int) -> str: ...
def slurp(file_path: str) -> str: ...
def update_title(content: str, title: str) -> str: ...