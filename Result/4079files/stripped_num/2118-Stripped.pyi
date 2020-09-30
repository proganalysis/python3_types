# (generated with --quick)

from typing import Any, Dict, List, Tuple, Union

BASE_DIR: str
BLASTN_SETS: BlastLimitSet
BLASTP_SETS: BlastLimitSet
BLASTX_SETS: BlastLimitSet
BLAST_CORRECT_PARAMS: str
BLAST_CORRECT_SEQ_ERROR_MSG: str
BLAST_CORRECT_SEQ_MAX_SEQ_NUMB_ERROR_MSG: str
BLAST_CORRECT_SEQ_TOO_SHORT_ERROR_MSG: str
BLAST_DB_NUCL_CHOICE: List[Tuple[str, str]]
BLAST_DB_NUCL_LIST: List[Dict[str, Union[bool, str]]]
BLAST_DB_PROT_CHOICE: List[Tuple[str, str]]
BLAST_DB_PROT_LIST: List[Dict[str, Union[bool, str]]]
BLAST_FORM_ATTRS: Dict[str, str]
BLAST_FORM_INPUTTEXT_ATTRS: Dict[str, str]
BLAST_MAX_NUMBER_SEQ_IN_INPUT: int
EVALUE_BLAST_DEFAULT: float
EVALUE_CHOICE_LIST: List[Tuple[Union[float, int], str]]
EVALUE_LIST: List[Union[float, int]]
EXAMPLE_FASTA_NUCL_FILE_PATH: str
EXAMPLE_FASTA_PROT_FILE_PATH: str
MATRIX_CHOICE_LIST: List[Tuple[str, str]]
MATRIX_DEFAULT: str
MATRIX_LIST: List[str]
NUCLEOTIDE_SEARCH_SENSITIVE_CHOICE: Tuple[Tuple[str, str], Tuple[str, str], Tuple[str, str]]
PROTEIN_SEARCH_SENSITIVE_CHOICE: Tuple[Tuple[str, str], Tuple[str, str], Tuple[str, str]]
SAMPLE_DIR: str
TBLASTN_SETS: BlastLimitSet
os: module

class BlastLimitSet(object):
    default_word_size: Any
    max_word_size: Any
    min_word_size: Any
    def __init__(self, default_word_size, min_word_size, max_word_size) -> None: ...
    def get_word_size_error(self) -> str: ...
