# (generated with --quick)

from typing import Any, List
import unittest.case

Molecule: Any
NwInput: Any
NwInputError: Any
NwOutput: Any
NwTask: Any
__author__: str
__copyright__: str
__date__: str
__email__: str
__maintainer__: str
__version__: str
coords: List[List[float]]
json: module
mol: Any
os: module
test_dir: str
unittest: module

class NwInputTest(unittest.case.TestCase):
    nwi: Any
    nwi_symm: Any
    def test_from_string_and_file(self) -> None: ...
    def test_str(self) -> None: ...
    def test_to_from_dict(self) -> None: ...

class NwOutputTest(unittest.case.TestCase):
    def test_get_excitation_spectrum(self) -> None: ...
    def test_parse_tddft(self) -> None: ...
    def test_read(self) -> None: ...

class NwTaskTest(unittest.case.TestCase):
    task: Any
    task_cosmo: Any
    task_esp: Any
    def test_dft_cosmo_task(self) -> None: ...
    def test_dft_task(self) -> None: ...
    def test_esp_task(self) -> None: ...
    def test_init(self) -> None: ...
    def test_multi_bset(self) -> None: ...
    def test_str_and_from_string(self) -> None: ...
    def test_to_from_dict(self) -> None: ...
