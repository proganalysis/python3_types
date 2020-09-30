from rx.core import Observable
from typing import Iterable

def _concat_with_iterable(sources: Iterable[Observable]) -> Observable: ...
