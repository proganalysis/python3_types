# (generated with --quick)

from typing import Any

BLAST_CORRECT_PARAMS: Any
BLAST_DB_NUCL_LIST: Any
BLAST_MAX_NUMBER_SEQ_IN_INPUT: Any
BlastForm: Any
BlastpForm: Any
BlastxForm: Any
EVALUE_BLAST_DEFAULT: Any
EXAMPLE_FASTA_NUCL_FILE_PATH: Any
EXAMPLE_FASTA_PROT_FILE_PATH: Any
NCBIXML: Any
NcbiblastnCommandline: Any
NcbiblastpCommandline: Any
NcbiblastxCommandline: Any
NcbitblastnCommandline: Any
TBlastnForm: Any
ast: module
os: module
render: Any
utils: Any

def blast(request, blast_form, template_init, template_result, blast_commandline, sample_fasta_path, extra_context = ...) -> Any: ...
def blastn(request, blast_form = ..., template_init = ..., template_result = ..., extra_context = ...) -> Any: ...
def blastp(request, blast_form = ..., template_init = ..., template_result = ..., extra_context = ...) -> Any: ...
def blastx(request, blast_form = ..., template_init = ..., template_result = ..., extra_context = ...) -> Any: ...
def tblastn(request, blast_form = ..., template_init = ..., template_result = ..., extra_context = ...) -> Any: ...
