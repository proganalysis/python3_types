# (generated with --quick)

from typing import Pattern

re: module

class Bbox(object):
    box_re: Pattern[str]
    float_re: str
    xmax: float
    xmin: float
    ymax: float
    ymin: float
    def __init__(self, from_string) -> None: ...
