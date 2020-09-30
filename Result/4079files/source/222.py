#!/usr/bin/python
# -*- coding: utf-8 -*-

from ..helper import EDBOWebApiHelper


class TestEDBOWebApiHelper(object):
    def test_format_file_size(self):
        assert EDBOWebApiHelper.format_file_size(1024, suffix='') == '1.0Ki'
        assert EDBOWebApiHelper.format_file_size(1024) == '1.0KiB'
