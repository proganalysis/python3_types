# (generated with --quick)

from typing import Any

models: Any
objectify: Any

class MxliffParser(object):
    __doc__: str
    content_key: str
    gloss_score_key: str
    mark_key: str
    score_key: str
    tunit_metadata_key: str
    type_key: str
    def parse(self, resource) -> list: ...
    def parse_group(self, group) -> Any: ...
    def parse_tunit_metadata(self, trans_unit) -> list: ...
