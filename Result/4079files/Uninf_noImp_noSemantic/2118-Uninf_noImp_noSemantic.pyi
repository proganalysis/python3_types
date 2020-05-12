from typing import Any

BASE_DIR: Any
SAMPLE_DIR: Any
BLAST_DB_NUCL_LIST: Any
BLAST_DB_PROT_LIST: Any
BLAST_DB_NUCL_CHOICE: Any
BLAST_DB_PROT_CHOICE: Any
EXAMPLE_FASTA_NUCL_FILE_PATH: Any
EXAMPLE_FASTA_PROT_FILE_PATH: Any
BLAST_MAX_NUMBER_SEQ_IN_INPUT: int
BLAST_FORM_ATTRS: Any
BLAST_FORM_INPUTTEXT_ATTRS: Any
MATRIX_LIST: Any
MATRIX_CHOICE_LIST: Any
MATRIX_DEFAULT: str
EVALUE_LIST: Any
EVALUE_CHOICE_LIST: Any
EVALUE_BLAST_DEFAULT: float
NUCLEOTIDE_SEARCH_SENSITIVE_CHOICE: Any
PROTEIN_SEARCH_SENSITIVE_CHOICE: Any

class BlastLimitSet:
    default_word_size: Any = ...
    min_word_size: Any = ...
    max_word_size: Any = ...
    def __init__(self, default_word_size: Any, min_word_size: Any, max_word_size: Any) -> None: ...
    def get_word_size_error(self): ...

BLASTN_SETS: Any
TBLASTN_SETS: Any
BLASTP_SETS: Any
BLASTX_SETS: Any
BLAST_CORRECT_SEQ_ERROR_MSG: str
BLAST_CORRECT_SEQ_MAX_SEQ_NUMB_ERROR_MSG: Any
BLAST_CORRECT_SEQ_TOO_SHORT_ERROR_MSG: str
BLAST_CORRECT_PARAMS: str
