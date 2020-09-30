'''
Created on 27.06.2017

@author: Peer
'''

from bson.code import Code
import os
import pathlib

import pymongo


TRANSLATION_TABLE = (('.', '\uff0e'),
                     ('$', '\uff04'))


class GitExplorerBase(object):

    @staticmethod
    def get_gitexplorer_database():
        '''Returns the MongoDB for gitexplorer.

        The collections inside the database can be used as basis for specialized collections
        from which one can derive elevated statistics. Results can also be written into the
        database to be accessible by visualization routines.
        '''
        client = pymongo.MongoClient()
        return client.gitexplorer_database

    @staticmethod
    def _mongodb_escape(input_string):
        for translation in TRANSLATION_TABLE:
            input_string = input_string.replace(translation[0], translation[1])
        return input_string

    @staticmethod
    def _mongodb_unescape(input_string):
        for translation in TRANSLATION_TABLE:
            input_string = input_string.replace(translation[1], translation[0])
        return input_string

    @staticmethod
    def _get_code(file_name):
        current_working_directory = pathlib.Path(os.getcwd())

        with (current_working_directory / file_name).open(mode='r') as fid:
            code = fid.read()

        return Code(code)
