# (generated with --quick)

from typing import Optional, Union

class QUICConection:
    handshake_count: int
    kDefaultInitialRtt: int
    kDelayedAckTimeout: int
    kMaxTLPs: int
    kMinRTOTimeout: int
    kMinTLPTimeout: int
    kReorderingThreshold: int
    kTimeReorderingFraction: float
    largest_sent_before_rto: Optional[int]
    loss_detection_alarm: None
    loss_time: Optional[int]
    reordering_threshold: Optional[Union[float, int]]
    rto_count: Optional[int]
    rttvar: Optional[int]
    sent_packets: None
    smoothed_rtt: Optional[int]
    time_reordering_fraction: Optional[float]
    tlp_count: Optional[int]
    def __init__(self) -> None: ...
