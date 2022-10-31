# (generated with --quick)

from typing import Any, Optional, Tuple

Comment: Any
Http404: Any
HttpResponsePermanentRedirect: Any
Page: Any
Paginator: Any
Q: Any
QuerySet: Any
Topic: Any
WSGIRequest: Any
reverse: Any
settings: Any

def _get_comment_pageid(qs_comments, comment_id: int, comments_per_page: int) -> int: ...
def _get_comments_per_page(request) -> int: ...
def _prefetch_for_comments(qs_comments) -> Any: ...
def _topic_comment_sanitize(request, comment_id: int) -> Tuple[Any, dict]: ...
def list_comments(request, topic_slug: str, comment_id: Optional[int] = ...) -> Tuple[Any, Any]: ...
def prev_comments_down(request, topic_slug: str, comment_id: int, scroll_to_id: int) -> Tuple[Any, Any]: ...
def replies_up(request, topic_slug: str, comment_id: int, scroll_to_id: int) -> Tuple[Any, Any]: ...
def replies_up_recursive(request, topic_slug: str, comment_id: int, scroll_to_id: int) -> Tuple[Any, Any]: ...