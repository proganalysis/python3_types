# coding=utf-8
import abc
import json
import logging
from pathlib import Path

import networkx

logger = logging.getLogger(__name__)


class ProtocolException(Exception):
    pass


class BaseRepository(abc.ABC):
    def __init__(self, absolute_path: Path):
        if not absolute_path.exists():
            logger.error("repository path `%s` does not exist", absolute_path.name)
            raise FileNotFoundError("repository path `%s` does not exist" % absolute_path.name)

        self._absolute_path = absolute_path

        if not self.info_path.exists():
            logger.error("`%s` is not a valid BiReUS repository", absolute_path.name)
            raise ValueError("`%s` is not a valid BiReUS repository" % absolute_path.name)

        logger.debug("Initialize Repository @ %s ", absolute_path)
        with self.info_path.open("r") as file:
            self._metadata = json.load(file)

        self.version_graph = networkx.read_gml(str(self.version_graph_path))  # type: networkx.Graph

    @property
    def absolute_path(self):
        return self._absolute_path

    @property
    @abc.abstractmethod
    def info_path(self) -> Path:
        pass

    @property
    @abc.abstractmethod
    def version_graph_path(self) -> Path:
        pass

    @property
    def name(self) -> str:
        return self._metadata['name']

    @property
    def first_version(self) -> str:
        return self._metadata['first_version']

    @property
    def latest_version(self) -> str:
        return self._metadata['latest_version']

    def has_version(self, name: str):
        return self.version_graph.has_node(name)

    @property
    def strategy(self) -> str:
        return self._metadata['strategy']

    @property
    def protocol(self) -> int:
        return self._metadata['protocol']
