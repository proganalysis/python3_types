class InvalidOperator(Exception):
    def __init__(self, e: KeyError) -> None: ...

class CustomValueError(Exception):
    def __init__(self) -> None: ...
