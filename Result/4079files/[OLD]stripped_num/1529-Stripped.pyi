# (generated with --quick)

from typing import List

class DisplaySegment(object):
    OFF_STR_HORIZ: str
    OFF_STR_VERT: str
    ON_STR_HORIZ: str
    ON_STR_VERT: str
    anode: bool
    cathodes: dict

class SevenSegmentDisplay(object):
    segments: List[DisplaySegment]
