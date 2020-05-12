from msa.core.event import Event

class TextInputEvent(Event):
    def __init__(self) -> None: ...

class TextOutputEvent(Event):
    def __init__(self) -> None: ...

class StyledTextOutputEvent(Event):
    def __init__(self) -> None: ...
