from typing import Any

first_num: Any
third_num: Any
fourth_num: Any

class FakeChromeUA:
    os_type: Any = ...
    chrome_version: Any = ...
    @classmethod
    def get_ua(cls): ...

headers: Any
