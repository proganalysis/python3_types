# -*- coding: utf-8 -*-
"""
    tests.item
    ---------------
    Test item of KINCluster
    :author: MaybeS(maytryark@gmail.com)
"""

import pytest

from KINCluster.core.item import Item

def test_item1() :
    """ Testing for item
    """
    assert Item(value="value") == Item(value="value")
    assert Item(value="value") != Item(value="not value")

    item = Item(value="val", string="str", integer="int")

    # assert str(item) == "int str val"
    assert set(item.values) == {'int', 'str', 'val'}
    assert set(item.keys) == {'integer', 'string', 'value'}