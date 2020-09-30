#!/usr/bin/python
# -*- coding: utf-8 -*-

from ..client import EDBOWebApiClient


class TestEDBOWebApiMethods(object):
    def setup(self):
        self.client = EDBOWebApiClient()

    def test_get_requests_list(self):
        requests_count = 100
        requests_list = self.client.get_requests_list(requests_count)

        assert self.client.get_status() == 200
        assert isinstance(requests_list, list)
        assert len(requests_list) == requests_count
