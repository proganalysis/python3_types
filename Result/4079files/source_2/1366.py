#!/usr/bin/env python3
import pymisp
import os

from typing import Union


class EmptySearchtermError(Exception):
    """Exception raised, when no saerch terms are given."""
    pass


class MISPClient:
    """The MISPClient class just hides the "complexity" of the queries. All params can be lists to query more than one
    MISP instance.

    :param url: URL of MISP instance
    :param key: API key
    :param ssl: Use/dont' use ssl or path to ssl cert if not possible to verify through trusted CAs
    :param name: Name of the MISP instance, is sent back in the report for matching the results."""

    def __init__(self, url: Union[list, str], key: Union[list, str], ssl: Union[list, bool]=True,
                 name: Union[list, str]='Unnamed'):
        self.misp_connections = []
        if type(url) is list:
            for idx, server in enumerate(url):
                verify = True
                if os.path.isfile(ssl[idx]):
                    verify = ssl[idx]
                self.misp_connections.append(pymisp.PyMISP(url=server,
                                                           key=key[idx],
                                                           ssl=verify))
        else:
            verify = True
            if os.path.isfile(ssl):
                verify = ssl
            self.misp_connections.append(pymisp.PyMISP(url=url,
                                                       key=key,
                                                       ssl=verify))
        self.misp_name = name

    @staticmethod
    def __misphashtypes() -> list:
        """Just for better readability, all __misp*type methods return just a list of misp data types

        :returns: MISP hash data types"""
        hashtypes = ['md5', 'sha1', 'sha256', 'ssdeep', 'sha224', 'sha384', 'sha512', 'sha512/224', 'sha512/256',
                     'tlsh', 'authentihash']
        filenames = []
        for h in hashtypes:
            filenames.append('filename|{0}'.format(h))
        return hashtypes + filenames

    @staticmethod
    def __mispurltypes() -> list:
        """Just for better readability, all __misp*type methods return just a list of misp data types

        :returns: misp url/domain data types"""
        return ['domain', 'domain|ip', 'url', 'link', 'named pipe', 'uri']

    @staticmethod
    def __mispdomaintypes() -> list:
        """Just for better readability, all __misp*type methods return just a list of misp data types

        :returns: data types containing domains"""
        return ['domain', 'hostname', 'domain|ip', 'email-src', 'email-dst', 'url', 'link', 'named pipe',
                'target-email', 'uri', 'whois-registrant-email', 'dns-soa-email', 'hostname|port', 'jabber-id']

    @staticmethod
    def __mispmailtypes() -> list:
        """Just for better readability, all __misp*type methods return just a list of misp data types

        :returns: misp mail data types"""
        return ['email-src', 'email-dst', 'target-email', 'email-subject', 'email-attachment', 'whois-registrant-email',
                'dns-soa-email', 'email-header']

    @staticmethod
    def __mispiptypes() -> list:
        """Just for better readability, all __misp*type methods return just a list of misp data types

        :returns: ip data types"""
        return ['ip-src', 'ip-dst', 'domain|ip', 'ip-src|port', 'ip-dst|port']

    @staticmethod
    def __mispregistrytypes() -> list:
        """Just for better readability, all __misp*type methods return just a list of misp data types

        :returns: misp regkey data types"""
        return ['regkey', 'regkey|value']
    
    @staticmethod
    def __mispfilenametypes() -> list:
        """Just for better readability, all __misp*type methods return just a list of misp data types

        :returns: data types containing filenames"""
        return ['filename', 'filename|md5', 'filename|sha1', 'filename|sha256', 'filename|ssdeep', 'filename|sha224',
                'filename|sha384', 'filename|sha512', 'filename|sha512/224', 'filename|sha512/256', 'filename|tlsh',
                'filename|authentihash']

    def __search(self, value: str, type_attribute: Union[list, None]):
        """Search method call wrapper.

        :param value: value to search for.
        :param type_attribute: attribute types to search for."""
        results = []
        if not value:
            raise EmptySearchtermError
        for idx, connection in enumerate(self.misp_connections):
            results.append({'url': connection.root_url,
                            'name': self.misp_name[idx],
                            'result': connection.search(type_attribute=type_attribute, values=value)})
        return results

    def search_url(self, searchterm: str) -> list:
        """Search for URLs"""
        return self.__search(type_attribute=self.__mispurltypes(), value=searchterm)

    def search_hash(self, searchterm: str) -> list:
        """Search for hashes"""
        return self.__search(type_attribute=self.__misphashtypes(), value=searchterm)

    def search_domain(self, searchterm: str) -> list:
        """Search for domains"""
        return self.__search(type_attribute=self.__mispdomaintypes(), value=searchterm)

    def search_mail(self, searchterm: str) -> list:
        """Search for emails"""
        return self.__search(type_attribute=self.__mispmailtypes(), value=searchterm)

    def search_ip(self, searchterm: str) -> list:
        """Search for ips"""
        return self.__search(type_attribute=self.__mispiptypes(), value=searchterm)

    def search_registry(self, searchterm: str) -> list:
        """Search for registry keys and values"""
        return self.__search(type_attribute=self.__mispregistrytypes(), value=searchterm)
    
    def search_filename(self, searchterm: str) -> list:
        """Search for filenames"""
        return self.__search(type_attribute=self.__mispfilenametypes(), value=searchterm)

    def searchall(self, searchterm: str) -> list:
        """Search through all attribute types, this could be really slow."""
        return self.__search(type_attribute=None, value=searchterm)
