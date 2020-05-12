# (generated with --quick)

import io
from typing import Any, TextIO, Type

BytesIO: Type[io.BytesIO]
apiKey: str
config: configparser.ConfigParser
configfile: TextIO
configparser: module
dataFolder: str
delta: Any
deltaFiles: Any
deltaUrl: str
file: Any
ini: str
json: module
latestFullData: Any
os: module
shutil: module
subprocess: module
sys: module
updateAvailable: bool
url: module
zipfile: module

def ProcessFile(datetime, insertUrl, updateUrl) -> None: ...
def extractZipFromUrl(urlStr) -> None: ...
def getLastUpdateTS() -> str: ...
