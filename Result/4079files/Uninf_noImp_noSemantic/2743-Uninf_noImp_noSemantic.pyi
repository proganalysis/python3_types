from typing import Any

def store_answer(qname: Any, qtype: Any, template: Any): ...
def resolver_init() -> None: ...
def get_templates(): ...
def generate_range(filename: Any, rng_templ: Any, entry_templ: Any): ...
def generate_step_query(tcurr: Any, id_prefix: Any): ...
def generate_step_check(id_prefix: Any): ...
def generate_step_elapse(tstep: Any, id_prefix: Any): ...
def main() -> None: ...
