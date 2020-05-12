from typing import Any

def parse_line(line: Any): ...

sites_filepath: Any
cpra_to_rsids_trie_filepath: Any
rsid_to_cpra_trie_filepath: Any

def should_replace(filepath: Any): ...
def run(argv: Any) -> None: ...
