from typing import Any

ALT_BASE_URL: Any
BASE_URL: Any
FILENAME: str
PACKAGE_PATH: str
JAVA_6_COMPATIBLE_VERSION: str
JAVA_7_COMPATIBLE_VERSION: str
LATEST_VERSION: str
JAVA_VERSION_REGEX: Any

def parse_java_version(version_text: Any): ...
def get_newest_possible_languagetool_version(): ...
def get_common_prefix(z: Any): ...
def download_lt(update: bool = ...) -> None: ...
