# (generated with --quick)

from typing import Any, Tuple

Case: Any
IntegerField: Any
Problem: Any
Sum: Any
User: Any
When: Any
_: Any
models: Any

class Blog(Any):
    Meta: type
    author: Any
    create_time: Any
    edit_time: Any
    hide_revisions: Any
    likes: Any
    objects: Any
    recommend: Any
    revisions: Any
    text: Any
    title: Any
    visible: Any

class BlogLikes(Any):
    BLOG_LIKE_FLAGS: Tuple[Tuple[str, str], Tuple[str, str]]
    Meta: type
    blog: Any
    flag: Any
    user: Any

class BlogQuerySet(Any):
    def with_dislikes(self) -> Any: ...
    def with_likes(self) -> Any: ...
    def with_likes_flag(self, user) -> Any: ...

class BlogRevision(Any):
    Meta: type
    author: Any
    create_time: Any
    text: Any
    title: Any

class Comment(Any):
    Meta: type
    author: Any
    blog: Any
    create_time: Any
    problem: Any
    text: Any
