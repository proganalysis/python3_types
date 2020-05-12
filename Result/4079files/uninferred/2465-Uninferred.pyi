from typing import Any

def configure_warnings(show_warnings: Any) -> None: ...
def kmer_lca(seqs_path: 'path to (optionally gzipped) fasta/fastq input', fastq: 'input is fastq; disable autodetection'=..., progress: 'show progress bar (sent to stderr)'=...) -> Any: ...
def annotate_diamond(fasta_path: 'path to fasta input', diamond_path: 'path to Diamond taxonomic classification output') -> Any: ...
def filter_taxa(fasta_path: 'path to fasta input', taxids: 'comma delimited list of taxon IDs', unclassified: 'pass sequences unclassified at superkingdom level >(0)'=..., discard: 'discard specified taxa'=..., warnings: 'show warnings'=...) -> Any: ...
def matrix(fasta_path: 'path to tictax annotated fasta input', scafstats_path: 'path to BBMap scaftstats file') -> Any: ...
def main() -> None: ...
