# (generated with --quick)

import requests.packages.urllib3.util.retry
import requests.sessions
from typing import Any, Callable, Dict, Generator, Optional, Pattern, Tuple, Type

Answer_Add_Comment_URL: str
Answer_Comment_Box_URL: str
Author_Get_More_Follow_Column_URL: str
Author_Get_More_Follow_Topic_URL: str
Author_Get_More_Followees_URL: str
Author_Get_More_Followers_URL: str
Cancel_Thanks_Url: str
Cancel_Unhelpful_Url: str
Captcha_URL: str
Column_API: str
Column_Data: str
Column_Post_Data: str
Column_Posts_Data: str
Column_Url: str
Default_Header: Dict[str, str]
Follow_Author_Url: str
Follow_Collection_Url: str
Follow_Question_Url: str
Follow_Topic_Url: str
Get_Answer_Comment_URL: str
Get_Collection_Url: str
Get_Me_Info_Url: str
Get_Profile_Card_URL: str
Login_URL: str
NavigableString: Any
PROTOCOL: str
Post_Get_Upvoter: str
Question_Get_More_Answer_URL: str
Retry: Type[requests.packages.urllib3.util.retry.Retry]
Send_Message_Url: str
Session: Type[requests.sessions.Session]
Tag: Any
Thanks_Url: str
Topic_Get_Children_Url: str
Topic_Get_More_Follower_Url: str
Topic_Hot_Questions_Url: str
Topic_Newest_Url: str
Topic_Questions_Url: str
Topic_Top_Answers_Url: str
Topic_Unanswered_Question_Url: str
Topic_Url: str
Unfollow_Collection_Url: str
Unhelpful_Url: str
Upvote_Answer_Url: str
Upvote_Article_Url: str
Zhihu_URL: str
_Bs: Any
functools: module
os: module
re: module
re_a2q: Pattern[str]
re_ans_url: Pattern[str]
re_author_url: Pattern[str]
re_collection_url: Pattern[str]
re_collection_url_split: Pattern[str]
re_column_url: Pattern[str]
re_del_empty_line: Pattern[str]
re_get_number: Pattern[str]
re_post_url: Pattern[str]
re_question_url: Pattern[str]
re_question_url_std: Pattern[str]
re_topic_url: Pattern[str]

def BeautifulSoup(makeup) -> Any: ...
def answer_content_process(content) -> Any: ...
def check_soup(attr, soup_type = ...) -> Callable[[Any], Any]: ...
def class_common_init(url_re, allowed_none = ..., trailing_slash = ...) -> Callable[[Any], Any]: ...
def clone_bs4_elem(el) -> Any: ...
def common_follower(url, xsrf, session) -> Generator[Any, Any, None]: ...
def get_path(path, filename, mode, default_path, default_name) -> Any: ...
def parser_author_from_comment(author) -> Tuple[Any, Any, str]: ...
def parser_author_from_tag(author) -> Tuple[Optional[str], Any, Any, str]: ...
def remove_invalid_char(text) -> str: ...
