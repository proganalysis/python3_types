# Copyright (C) 2016 Simon Dirmeier
#
# This file is part of rnaiutilities.
#
# rnaiutilities is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rnaiutilities is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rnaiutilities. If not, see <http://www.gnu.org/licenses/>.
#
# @author = 'Simon Dirmeier'
# @email = 'simon.dirmeier@bsse.ethz.ch'


import logging

from rnaiutilities.plate.plate_layout import PlateLayout

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LibraryPlateLayout:
    """
    Class that loads the layout meta files for the plates, i.e. which siRNAs
    map to which well, etc.

    """

    def __init__(self, file):
        """
        Constructor for the meta file loader from an open-bis instance,
        e.g.: target_infect_x_library_layouts_beautified.tsv

        :param file: the layout meta file
        :param pattern: the patterns you are searching for
        """

        self._meta_file = file
        self._meta = {}
        logger.info("Loading layout...")
        self._load()

    def _load(self):
        with open(self._meta_file, "r") as f:
            for entry in f.readlines():
                entry = entry.lower()
                if entry.startswith("barcode"):
                    continue
                tokens = entry.strip().split("\t")
                self._add(tokens)

    def _add(self, tokens):
        bar, expr, _, geneset, _, library, _, _, well, \
         well_type, gene, sirna = tokens
        classifier = (expr + "-" + bar)
        if classifier not in self._meta:
            self._meta[classifier] = PlateLayout(classifier, geneset, library)
        self._meta[classifier].add(gene, sirna, well, well_type)

    def get(self, pathogen, library, design, screen, replicate, plate, suffix):
        """
        Get the layout for a specific plate.

        :param pathogen: the pathogen, e.g. BRUCELLA
        :param library: the library, e.g. DP
        :param screen: replicate, e.g D
        :param replicate: replicate, e.g 1
        :param plate: the plate, e.g. DZ44-1K
        :param suffix: the suffix, e.g. BASEL, otherwise None
        :return: returns a PlateLayout
        """

        # TODO: this should be ok, but is potentially
        #  buggy with the suffix thing.
        if suffix is None or suffix is 'NA':
            cl = "-".join([pathogen,
                           "".join([library, design]),
                           "".join([screen, replicate]),
                           plate]).lower()
        else:
            cl = "-".join([pathogen,
                           "".join([library, design]),
                           "".join([screen, replicate]),
                           suffix,
                           plate]).lower()
        if cl in self._meta:
            return self._meta[cl]
        logger.warning("Did not find " + cl + " in layout file")
        return None
