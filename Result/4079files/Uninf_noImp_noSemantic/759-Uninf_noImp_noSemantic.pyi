from config import *
from core.framework.common import *
from core.model import *
from typing import Any, Optional

class VariantManager:
    def __init__(self) -> None: ...
    def get(self, reference_id: Any, variant_id: Any, analysis_id: Optional[Any] = ...): ...
