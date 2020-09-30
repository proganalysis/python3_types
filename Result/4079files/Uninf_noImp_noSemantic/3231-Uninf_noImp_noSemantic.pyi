import numpy as np
from aiohttp import web
from typing import Any

nsfw_net: Any
caffe_transformer: Any

def classify(image: bytes) -> np.float64: ...
async def fetch(session: Any, url: Any): ...

class API(web.View):
    async def post(self): ...

session: Any
app: Any
