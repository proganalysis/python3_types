# (generated with --quick)

from typing import Any, Dict, Optional

MorphPossibilityObject: Any
dbHeadwordObject: Any
dbWordCountObject: Any
findcountsviawordcountstable: Any
hipparchia: Any
re: module
session: Any

def formatdictionarysummary(wordentryobject) -> str: ...
def formatparsinginformation(possibilitieslist) -> str: ...
def formatprevalencedata(wordcountobject) -> str: ...
def getobservedwordprevalencedata(dictionaryword) -> Optional[str]: ...
def lexicaldbquickfixes(listofnames) -> Dict[Any, str]: ...
