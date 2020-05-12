from typing import Any

BeautifulSoup: Any
Default_Header: Any
Zhihu_URL: str
Login_URL: Any
Captcha_URL: Any
Get_Profile_Card_URL: Any
Question_Get_More_Answer_URL: Any
Answer_Add_Comment_URL: Any
Answer_Comment_Box_URL: Any
Get_Answer_Comment_URL: Any
Author_Get_More_Followers_URL: Any
Author_Get_More_Followees_URL: Any
Author_Get_More_Follow_Column_URL: Any
Author_Get_More_Follow_Topic_URL: Any
PROTOCOL: str
Column_Url: str
Column_API: Any
Column_Data: Any
Column_Posts_Data: Any
Column_Post_Data: Any
Post_Get_Upvoter: Any
Topic_Url: Any
Topic_Get_Children_Url: Any
Topic_Get_More_Follower_Url: Any
Topic_Questions_Url: Any
Topic_Unanswered_Question_Url: Any
Topic_Top_Answers_Url: Any
Topic_Hot_Questions_Url: Any
Topic_Newest_Url: Any
Get_Me_Info_Url: Any
Upvote_Answer_Url: Any
Upvote_Article_Url: Any
Follow_Author_Url: Any
Follow_Question_Url: Any
Follow_Topic_Url: Any
Follow_Collection_Url: Any
Unfollow_Collection_Url: Any
Thanks_Url: Any
Cancel_Thanks_Url: Any
Send_Message_Url: Any
Unhelpful_Url: Any
Cancel_Unhelpful_Url: Any
Get_Collection_Url: Any
re_question_url: Any
re_question_url_std: Any
re_ans_url: Any
re_author_url: Any
re_collection_url: Any
re_column_url: Any
re_post_url: Any
re_topic_url: Any
re_a2q: Any
re_collection_url_split: Any
re_get_number: Any
re_del_empty_line: Any

def check_soup(attr: Any, soup_type: str = ...): ...
def class_common_init(url_re: Any, allowed_none: bool = ..., trailing_slash: bool = ...): ...
def remove_invalid_char(text: Any): ...
def parser_author_from_tag(author: Any): ...
def parser_author_from_comment(author: Any): ...
def answer_content_process(content: Any): ...
def get_path(path: Any, filename: Any, mode: Any, default_path: Any, default_name: Any): ...
def common_follower(url: Any, xsrf: Any, session: Any) -> None: ...
def clone_bs4_elem(el: Any): ...
