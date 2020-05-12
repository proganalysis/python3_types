#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017/1/29 21:18
# Project: turboPydDNS
# __author__ = 'ihipop'

from abc import ABCMeta,abstractmethod
import ddns
import urllib.parse,platform

import requests
import logging

logger = logging.getLogger(__name__)

class BaseUpdater(metaclass=ABCMeta):
    _useragent = 'turboPydDNS %s/V%s ihipop+turboPydDNS@gmail.com' % (platform.system(),ddns.__version__)
    _externalIp = None

    @abstractmethod
    def build_payload(self):
        pass

    @abstractmethod
    def parse_result(self,response):
        pass

    @abstractmethod
    def updater(self):
        pass

    @classmethod
    def get_external_ip(self):
        try:
            r = requests.get('https://httpbin.org/ip',headers={"User-Agent": self._useragent})
            r = r.json()['origin']
        except:
            return  None

class BaseHTTPUpdater(BaseUpdater):
    _api_url = None
    _query = {}
    _data = {}
    _headers = {}

    def __int__(self,*args, **kwargs):
        api_url = kwargs['api_url']
        if api_url:
            self._api_url=api_url
        if isinstance(kwargs.get('query'),dict):
            self._query.update(kwargs.get('query',{}))
        if isinstance(kwargs.get('data'),dict):
            self._data.update(kwargs.get('data',{}))
        pass

    @abstractmethod
    def build_payload(self):
        url = self._api_url + '?' if '?' not in self._api_url else '&'
        url = url + urllib.parse.urlencode(self._query)
        if self._useragent:
            self._headers.update({"User-Agent": self._useragent})
        payload = {
            'url': url,
            'data': self._data,
            'auth': None,
            'headers': self._headers
        }
        return payload

    def updater(self):
        payload = self.build_payload()
        timeout = 60
        try:
            if payload['data']:
                r = requests.post(payload['url'], data=payload['data'], headers=payload['headers'],
                                  auth=payload['auth'], timeout=timeout)
            else:
                r = requests.get(payload['url'], headers=payload['headers'], auth=payload['auth'], timeout=timeout)
            return self.parse_result(r)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as exc:
            msg = "an error occurred while updating IP at '%s'" % payload['url']
            logging.warning(msg, exc_info=exc)
            return (False, msg)

class Base3FactsHTTPUpdater(BaseHTTPUpdater):
    _username = None
    _password = None
    _hostname = None

    def __init__(self,hostname,username,password,*args, **kwargs):
        for k,v in {'hostname':hostname,'username':username,'password':password}.items():
            if  not k :
                raise Exception(k + ' Must be set')
            else:
                setattr(self,'_'+k,v)
        super().__init__()


    def build_payload(self):
        payload = super().build_payload()
        if self._username and self._password:
            payload['auth'] = (self._username, self._password)
        return payload

