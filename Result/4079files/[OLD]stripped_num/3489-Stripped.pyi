# (generated with --quick)

import requests.sessions
from typing import Optional, Pattern, Type
import xml.etree.ElementTree

ET: module
base64: module
collections: module
datetime: Type[datetime.datetime]
hashlib: module
hmac: module
os: module
rank_search: Pattern[str]
re: module
requests: module
session: Optional[requests.sessions.Session]
urllib: module

def download_aws_rank(url) -> int: ...
def get_awi_url_info(url) -> xml.etree.ElementTree.Element: ...
def get_rank(url) -> int: ...
