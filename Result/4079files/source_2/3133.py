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

"""This method provides the function `add_test` that creates the necesary files
to add a new custom test case to the database folder
"""

from glob import glob
from logging import getLogger
from os import makedirs, remove
from os.path import isdir, basename
from re import search
from sys import stdin

LOG = getLogger('jutge.add_test')


def add_test(database: str, code: str, delete: 'Boolean' = False,
             input_file=stdin, output_file=stdin,
             inp_suffix: str = 'inp', cor_suffix: str = 'cor', **kwargs):
    """Add custom test to database

    :param database: database folder path
    :param code: problem code
    :param delete: if true, delete tests of problem
    :param input_file: file containing test case input
    :param output_file: file containing test case output
    :param inp_suffix: input file suffix
    :param cor_suffix: output file suffix
    """

    dest_folder = '{}/{}'.format(database, code)

    if delete:  # Delete all custom test cases and return
        for custom_test in glob('{}/custom-*'.format(dest_folder)):
            remove(custom_test)
        return

    # input from stdin if no file provided
    if input_file == stdin:
        print('Enter input: (^D to end input)')
    src_inp = input_file.read()
    if output_file == stdin:
        print('Enter output: (^D to end input)')
    src_cor = output_file.read()

    if not isdir(dest_folder):
        makedirs(dest_folder)

    # sorted sorts the output alfabetically since glob does not
    files = sorted(glob('{}/custom-*'.format(dest_folder)))
    if files:
        # find the number of the last custom test and add 1 to it
        num = 1 + int(search(r'-([0-9]*)\.', basename(files[-1])).group(1))
    else:
        # if there are no custom tests yet, start by 0
        num = 0

    dest = '{folder}/custom-{n:02}'.format(folder=dest_folder, n=num)

    LOG.debug(dest)

    with open('{}.{}'.format(dest, inp_suffix), 'w') as inp_file:
        inp_file.write(src_inp)
    with open('{}.{}'.format(dest, cor_suffix), 'w') as cor_file:
        cor_file.write(src_cor)
