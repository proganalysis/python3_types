# (generated with --quick)

import distutils.errors
from typing import Any, Dict, Type
import unittest.case

BuildManPage: Any
Distribution: Any
DistutilsOptionError: Type[distutils.errors.DistutilsOptionError]
ManPageFormatter: Any
app_description: str
app_long_description: str
app_name: str
argparse: module
datetime: module
make_temp: Any
section_name: str
section_text: str
sections: Dict[str, str]
unittest: module

class BuildManPageTest(unittest.case.TestCase):
    def test_finalize_options(self) -> None: ...

class ManPageFormatterTest(unittest.case.TestCase):
    def test_format_functions(self) -> None: ...
    def test_formatter(self) -> None: ...
    def test_mk_description(self) -> None: ...
    def test_mk_footer(self) -> None: ...
    def test_mk_name(self) -> None: ...
    def test_mk_options(self) -> None: ...
    def test_mk_synopsis(self) -> None: ...
    def test_mk_title(self) -> None: ...

def test_arg_parser(formatter_class = ...) -> argparse.ArgumentParser: ...
