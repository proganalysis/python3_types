# -*- coding: utf-8 -*-
r"""
Test for latex prints
"""
# Author: Óscar Nájera

import pyutils.latex_print as lp


def test_ket():
    assert lp.ket(0) == r"|\emptyset\rangle"
    assert lp.ket(1) == r"|\downarrow\rangle"
    assert lp.ket(2) == r"|\uparrow\rangle"
    assert lp.ket(3) == r"|\uparrow \downarrow\rangle"
