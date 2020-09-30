# (generated with --quick)

import __builtin__
from typing import Any, List, Optional

cache: Any
uuid: module

class Alignment(object):
    __doc__: str
    hit_def: Any
    hit_protein_name: str
    hit_url: str
    hsp_list: List[nothing]
    length: Any
    title: Any
    def __init__(self, **kwargs) -> None: ...
    def best_evalue(self) -> None: ...
    def best_identities(self) -> Optional[float]: ...
    def best_score(self) -> None: ...
    def get_id(self) -> int: ...

class BlastRecord(object):
    __doc__: str
    alignments: List[nothing]
    application: Any
    expect: Any
    query: Any
    reference: Any
    version: Any
    def __init__(self, **kwargs) -> None: ...

class Hsp(object):
    __doc__: __builtin__.str
    align_length: Any
    bits: float
    expect: Any
    frame: Any
    gaps: Any
    identities: Any
    limit_length: int
    match: Any
    num_alignments: Any
    positives: Any
    query: Any
    query_end: Any
    query_start: Any
    sbjct: Any
    sbjct_end: Any
    sbjct_start: Any
    score: Any
    str: Any
    strand: Any
    def __init__(self, **kwargs) -> None: ...
    def chop_match(self) -> Any: ...
    def chop_query(self) -> Any: ...
    def chop_sbjct(self) -> Any: ...
    @staticmethod
    def chop_sequence(sequence, limit_length) -> list: ...
    def get_hsp_key_from_cache(self) -> __builtin__.str: ...
    def get_query_key_from_cache(self) -> __builtin__.str: ...
    @staticmethod
    def get_set_key(prefix, value_to_set) -> Any: ...
    def get_subject_key_from_cache(self) -> __builtin__.str: ...
    def get_tabular_str(self) -> __builtin__.str: ...
