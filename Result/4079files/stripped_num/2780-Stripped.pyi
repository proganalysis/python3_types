# (generated with --quick)

from typing import Type
import unittest.case

TestCase: Type[unittest.case.TestCase]

class ExtendedTestCase(unittest.case.TestCase):
    def assertLemmatisationEqual(self, origin, result, message = ..., _lemma_obj = ...) -> None: ...
    def assertLemmatisationMultipleEqual(self, origin, result, message = ..., _lemma_obj = ...) -> None: ...
