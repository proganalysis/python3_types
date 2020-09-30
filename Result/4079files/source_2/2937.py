'''
Created on 15.08.2017

@author: Peer Wagner
'''

import importlib

from gitexplorer import basics


class AggregatorRegistry(type):

    aggregators = {}

    def __new__(cls, name, bases, dct):
        cls_obj = super(AggregatorRegistry, cls).__new__(cls, name, bases, dct)

        if(isinstance(cls_obj.name, str)):
            cls.aggregators[cls_obj.name] = cls_obj

        return cls_obj

    @classmethod
    def get(cls, name):
        return cls.aggregators[name]

    @classmethod
    def load(cls, *aggregator_modules):
        for aggregator_module in aggregator_modules:
            importlib.import_module(aggregator_module)


class AbstractAggregator(basics.GitExplorerBase, metaclass=AggregatorRegistry):

    @property
    def name(self):
        raise NotImplementedError()

    def provides(self) -> str:
        raise NotImplementedError()

    def requires(self) -> str:
        raise NotImplementedError()

    def run(self):
        gitexplorer_database = self.get_gitexplorer_database()
        gitexplorer_database[self.output_database].drop()
        gitexplorer_database[self.input_database].aggregate(self.pipeline)
