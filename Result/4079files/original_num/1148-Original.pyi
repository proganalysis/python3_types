# (generated with --quick)

from typing import Any, List

AGGREGATES_DEFAULT_VARS: List[str]
COUNTRY_DIR: str
DATA_DIR: str
common: module
france_data_tax_benefit_system: openfisca_france_data
id_variables: Any
inspect: module
log: logging.Logger
logging: module
openfisca_france: Any
openfisca_france_tax_benefit_system: Any
os: module
pandas: Any
pkg_resources: module
reforms: Any
survey_variables: module
variables: list

class openfisca_france_data(Any):
    def apply(self) -> None: ...

def CountryTaxBenefitSystem() -> openfisca_france_data: ...
def __getattr__(name) -> Any: ...
def get_variables_from_module(module) -> list: ...
def get_variables_from_modules(modules) -> list: ...
def impute_take_up(target_probability, eligible, weights, recourant_last_period, seed) -> Any: ...
def select_to_match_target(target_probability = ..., target_mass = ..., eligible = ..., weights = ..., take = ..., seed = ...) -> Any: ...
