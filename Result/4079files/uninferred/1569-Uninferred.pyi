from prices import percentage_discount as percentage_discount
from typing import Any

RATES: Any

def base_currency(db: Any, settings: Any) -> None: ...
def conversion_rates(db: Any): ...
def test_conversionrate__str_repr(conversion_rates: Any) -> None: ...
def test_the_same_currency_uses_no_conversion() -> None: ...
def test_base_currency_to_another() -> None: ...
def test_convert_other_currency_to_base_currency() -> None: ...
def test_two_base_currencies_the_same_currency_uses_no_conversion() -> None: ...
def test_convert_two_non_base_currencies() -> None: ...
def test_exchange_currency_uses_passed_conversion_rate() -> None: ...
def test_two_base_currencies_convert_price_uses_passed_conversion_rate() -> None: ...
def test_exchange_currency_for_money_range() -> None: ...
def test_exchange_currency_for_money_range_uses_passed_conversion_rate() -> None: ...
def test_exchange_currency_for_taxed_money() -> None: ...
def test_exchange_currency_for_taxed_money_uses_passed_conversion_rate() -> None: ...
def test_exchange_currency_for_taxed_money_range() -> None: ...
def test_exchange_currency_for_taxed_money_range_uses_passed_conversion_rate() -> None: ...
def test_exchange_currency_raises_for_nonsupported_type() -> None: ...
def test_template_filter_money_in_currency() -> None: ...
def test_get_rates_caches_results(conversion_rates: Any) -> None: ...
def test_get_rates_force_update_cache(conversion_rates: Any) -> None: ...
