# (generated with --quick)

from typing import Any

Keys: Any
WebDriverWait: Any
settings: Any
time: module
webdriver: Any

class WorkflowyScheduler(object):
    browser: Any
    workflowy_url: str
    @classmethod
    def _WorkflowyScheduler__click_button(cls, css_selector) -> None: ...
    @classmethod
    def _WorkflowyScheduler__fill_text_box(cls, css_selector, text_to_input) -> None: ...
    @classmethod
    def _WorkflowyScheduler__get_todays_date_tag(cls) -> str: ...
    @classmethod
    def _WorkflowyScheduler__login(cls) -> None: ...
    @classmethod
    def _WorkflowyScheduler__mark_results_with_tag(cls, tag) -> None: ...
    @classmethod
    def _WorkflowyScheduler__save_changes(cls) -> None: ...
    @classmethod
    def _WorkflowyScheduler__search(cls, search_term) -> None: ...
    @classmethod
    def _WorkflowyScheduler__wait_for_element_to_appear(cls, css_selector) -> None: ...
    @classmethod
    def schedule_items_for_today(cls) -> None: ...
