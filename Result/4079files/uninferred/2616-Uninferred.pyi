from typing import Any

deltaUrl: str
ini: str
dataFolder: str
updateAvailable: bool

def getLastUpdateTS(): ...
def extractZipFromUrl(urlStr: Any) -> None: ...
def ProcessFile(datetime: Any, insertUrl: Any, updateUrl: Any) -> None: ...

config: Any
apiKey: Any
delta: Any
deltaFiles: Any
latestFullData: Any
