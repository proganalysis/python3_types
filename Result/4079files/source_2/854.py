# -*- coding: utf-8 -*-
"""
CSGO's informations displayed on an Arduino featuring a bomb timer.

@auteur: tsuriga, Darkness4
"""

from sys import argv, exit
from qtpy.QtWidgets import QApplication # type: ignore

# from .appui import Csgogsi
from appui import Csgogsi


def main():
    """Launch."""
    app = None
    app = QApplication(argv)
    ex = Csgogsi()
    exit(app.exec_())
