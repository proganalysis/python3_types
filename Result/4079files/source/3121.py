#!/usr/bin/python3

# Copyright (C) 2017  Aleix Boné (abone9999 at gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Provides function to download problem files to database
"""

from importlib.util import find_spec
from logging import getLogger
from os import makedirs
from os.path import isdir, isfile
from tempfile import NamedTemporaryFile
from zipfile import ZipFile, BadZipFile

from bs4 import BeautifulSoup
from requests import get
from requests.exceptions import ConnectionError

PARSER = 'lxml' if find_spec('lxml') is not None else 'html.parser'

LOG = getLogger('jutge.download')


def download(code: str, cookies: dict, database: str,
             no_download: 'Boolean' = False, overwrite: 'Boolean' = False,
             **kwargs):
    """Download problem files to database

    :param code: problem code
    :param cookies: cookies used to connect
    :param database: database folder
    :param no_download: do not connect to jutge.org
    :param overwrite: overwrite already existing files in database
    """


    LOG.debug(code)
    web = 'https://jutge.org/problems/{}'.format(code)

    LOG.debug(cookies)

    # Check if already in DB
    db_folder = '{}/{}'.format(database, code)
    LOG.debug(db_folder)

    if not isdir(db_folder) or overwrite:

        if no_download:
            LOG.error('Remove --no-download flag to download')
            return

        if code[0] == 'X':
            if cookies == {}:
                LOG.error('Cookie needed to download problem')
                return

        zip_url = '{}/zip'.format(web)
        LOG.debug(zip_url)

        try:
            response = get(zip_url, cookies=cookies, stream=True)
        except ConnectionError:
            LOG.error('Connection Error, are you connected to the internet?')
            exit(1)
        with NamedTemporaryFile('r+b', suffix='.zip', delete=False) as tmp_zip:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    tmp_zip.write(chunk)

            tmp_zip.close()

            try:
                zip_file = ZipFile(tmp_zip.name, 'r')
            except BadZipFile:
                LOG.error('Could not download zip file')
                exit(23)

        if not isdir(db_folder):
            makedirs(db_folder)

        zip_file.extractall(db_folder + '/..')
        zip_file.close()
    else:
        LOG.warning('Folder already in DB, use overwrite to force download')

    if isfile('{}/problem.html'.format(db_folder)) and not overwrite:
        LOG.info('File already in DB, continue')
        return

    if no_download:
        LOG.error('Remove --no-download flag to download')
        return

    if code[0] == 'X':
        if cookies == {}:
            LOG.error('Cookie needed to download problem')
            return


    try:
        response = get(web, cookies=cookies)
    except ConnectionError:
        LOG.error('Connection Error, are you connected to the internet?')
        return

    soup = BeautifulSoup(response.text, PARSER)

    name = '-'.join(soup.find('title').text.split('-')[1:])
    name = name[1:].replace(' ', '_').split()[0]
    if name == 'Error':
        LOG.error("Couldn't download page, aborting...")
        return

    # Delete token uid from database (if found)
    try:
        soup.find('input', {'name' : 'token_uid'})['value'] = ''
    except TypeError:
        pass

    with open('{}/problem.html'.format(db_folder), 'w') as problem_file:
        problem_file.write(str(soup))
