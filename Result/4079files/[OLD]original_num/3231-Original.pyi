# (generated with --quick)

from typing import Any, Tuple

HTTPBadRequest: Any
HTTPNotFound: Any
HTTPUnsupportedMediaType: Any
aiohttp: Any
app: Any
async_timeout: Any
asyncio: module
caffe_transformer: Any
np: module
nsfw_net: Any
session: Any
uvloop: Any
web: Any

class API(Any):
    def post(self) -> coroutine: ...

def caffe_preprocess_and_compute(pimg, caffe_transformer = ..., caffe_net = ..., output_layers = ...) -> Any: ...
def classify(image: bytes) -> Any: ...
def fetch(session, url) -> coroutine: ...
def load_model(model_def = ..., pretrained_model = ...) -> Tuple[Any, Any]: ...
