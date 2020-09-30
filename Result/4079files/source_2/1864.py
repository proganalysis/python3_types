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

"""Method to login and save a cookie file
"""

from getpass import getpass
from logging import getLogger

from requests import Session
from requests.exceptions import ConnectionError
from requests.utils import dict_from_cookiejar

from .cookie import Cookie

LOG = getLogger('jutge.login')


def login(email: str, password: str, prompt: 'Boolean', quiet: 'Boolean',
          no_download: 'Boolean', **kwargs):
    """Login to jutge.org

    :param email: login email
    :param password: login password
    :param prompt: if True force prompt to user
    :param quiet: supress output
    :param no_download: do not connect to jutge.org
    """

    if email is None or prompt:
        email = input('Email: ')
    else:
        if not quiet:
            print('Email :', email)

    if password is None or prompt:
        password = getpass('Password: ')

    url = 'https://jutge.org/'
    login_data = {
        'email': email,
        'password': password,
        'submit': ''
    }
    try:
        sess = Session()
        sess.post(url, data=login_data)
        session_cookie = dict_from_cookiejar(sess.cookies)['PHPSESSID']
    except ConnectionError:
        LOG.error('Connection Error, are you connected to the internet?')
        exit(1)
    finally:
        sess.close()

    LOG.debug(session_cookie)

    Cookie(cookie=session_cookie, no_download=no_download,
           skip_check=False, **kwargs)
