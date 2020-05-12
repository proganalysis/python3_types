# (generated with --quick)

import point_charges_2D
from typing import Type

Charge: Type[point_charges_2D.Charge]

def line_charge(parametric_x, parametric_y, trange, res, Q) -> None: ...
def rectangle_charge(dim, corner, res, Q) -> None: ...
def straight_line_charge(start, end, res = ..., Q = ...) -> None: ...
