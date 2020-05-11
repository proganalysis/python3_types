#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017/1/29 22:02
# Project: turboPydDNS
# __author__ = 'ihipop'

from .base import BaseHTTPUpdater
import requests

import logging

logger = logging.getLogger(__name__)


class DuckDNSUpdater(BaseHTTPUpdater):
    '''
    https://{DOMAIN}/update?domains={DOMAINLIST}&token={TOKEN}&ip={IP}
    DOMAIN the service domain
    DOMAINLIST is either a single domain or a comma separated list of domains
    TOKEN is the API token for authentication/authorization
    IP is either the IP or blank for auto-detection
    '''
    _api_url = 'https://www.duckdns.org/update'
    _domains = None
    _token = None

    info_code = {
        "OK": "Success.",
        "KO": "Fail.",
    }

    def __init__(self, domains, token, *args, **kwargs):
        for k, v in {'domains': domains, 'token': token, }.items():
            if not k:
                raise Exception(k + ' Must be set')
            else:
                setattr(self, '_' + k, v)
        super().__init__()

    def build_payload(self):
        self._query.update({'domains': self._domains,
                            'token': self._token
                            })
        # print(self._query)
        return super().build_payload()

    def parse_result(self, response: requests.models.Response):
        logger.debug('Got Response: %s' % response.text.strip())
        text = response.text.strip()
        success = False
        if response.status_code == 200:
            if text == 'OK':
                success = True
            msg = self.info_code.get(text, text) + ' (%s)' % text
        else:
            msg = 'invalid http status code: %s' % response.status_code
        return (success, msg)
