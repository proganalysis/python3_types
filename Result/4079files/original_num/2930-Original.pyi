# (generated with --quick)

from typing import Any

BaseScraper: Any
Document: Any
IntegrityError: Any
ensure_absolute_url: Any
html: module
log: logging.Logger
logging: module
parse: module
scrapelib: Any

class KnoxCoTNAgendaScraper(Any):
    MEETING_SCHEDULE_URL: str
    SITE_ROOT_URL: str
    scraper: Any
    def __init__(self) -> None: ...
    def _get_docs_from_schedule(self, page_str) -> list: ...
    def scrape(self, session) -> None: ...
