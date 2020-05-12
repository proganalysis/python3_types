from config import *
from core.framework.common import *
from core.framework.tus import *
from core.model import *
from api_rest.rest import *
from typing import Any

class VariantHandler:
    @staticmethod
    def get(request: Any): ...
    @staticmethod
    async def new(request: Any): ...
