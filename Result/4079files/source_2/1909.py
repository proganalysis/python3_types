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

from rnaiutilities.utility.array import unique


class TableFileSet:
    def __init__(self, key, query_result, features, **kwargs):
        self._table_file_set_classifier = key
        f = [x[-1].replace("_meta.tsv", "") for x in query_result]
        self.file_names = unique([el + "_data.tsv" for el in f])
        self._feature_classes = unique([x[7] for x in query_result])
        self._filesuffixes = unique([x.split("/")[-1] for x in f])
        self._feature_list_table = unique([
            suf.replace("-", "_") for suf in self._filesuffixes])
        self._features = set(features)
        self._filter = kwargs
        self._study, self._pathogen, self._lib, \
          self._design, self._replicate,\
          self._plate = query_result[0][1:7]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Tablefile: " + self._table_file_set_classifier

    def detail(self):
        s = "\n" + self.__str__() + "\n"
        s += "\tFiles:\t" + "\n\t\t".join(self.file_names) + "\n"
        s += "\tFeature-classes:\t" + ",".join(self._feature_classes) + "\n"
        s += "\tFeaturelist table:\t" + ",".join(self._feature_list_table) + "\n"
        return s

    def __eq__(self, other):
        if not isinstance(other, TableFileSet):
            return False
        return self.file_names == other.file_name

    def __hash__(self):
        return hash(self.file_names)

    @property
    def classifier(self):
        return self._table_file_set_classifier

    @property
    def features(self):
        return self._features

    @property
    def filenames(self):
        return self.file_names

    @property
    def feature_classes(self):
        return self._feature_classes

    @property
    def filesuffixes(self):
        return self._filesuffixes

    @property
    def study(self):
        return self._study

    @property
    def pathogen(self):
        return self._pathogen

    @property
    def library(self):
        return self._lib

    @property
    def design(self):
        return self._design

    @property
    def replicate(self):
        return self._replicate

    @property
    def plate(self):
        return self._plate
