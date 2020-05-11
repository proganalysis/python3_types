# (generated with --quick)

from typing import Any

RRTStar: Any
path_cost: Any
random: module

class RRTStarBidirectional(Any):
    c_best: Any
    sigma_best: Any
    swapped: bool
    x_goal: Any
    x_init: Any
    def __init__(self, X, Q, x_init, x_goal, max_samples, r, prc = ..., rewire_count = ...) -> None: ...
    def connect_trees(self, a, b, x_new, L_near) -> None: ...
    def rrt_star_bidirectional(self) -> Any: ...
    def swap_trees(self) -> None: ...
    def unswap(self) -> None: ...
