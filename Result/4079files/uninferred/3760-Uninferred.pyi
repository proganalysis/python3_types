from typing import Any, IO, Union

__author__: str
__version__: str
__date__: str
__revision__: str
__license__: str

def hide(input_image: Union[str, IO[bytes]], message: str) -> Any: ...
def reveal(input_image: Union[str, IO[bytes]]) -> Any: ...
