from japronto.router import Router as Router
from japronto.router.cmatcher import Matcher as Matcher
from typing import Any

def slash(request: Any): ...
def hello(request: Any): ...
async def sleep(request: Any): ...
async def loop(request: Any): ...
def dump(request: Any): ...

app: Any
r: Any