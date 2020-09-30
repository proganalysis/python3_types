# (generated with --quick)

from typing import Any, Dict, List, Tuple, TypeVar, Union

ERROR_LOGGER: Any
EntityExtractorWorker: Any
FACT_FIELD: Any
json: module
logging: module
np: module

_T0 = TypeVar('_T0')

class EntityExtractorPreprocessor(object):
    __doc__: str
    _feature_map: Any
    def __init__(self, feature_map = ...) -> None: ...
    def _preds_to_doc(self, doc, result_doc, field) -> Tuple[List[Dict[str, Any]], int]: ...
    def transform(self, documents: _T0, **kwargs) -> Dict[str, Union[Dict[str, Any], _T0]]: ...
