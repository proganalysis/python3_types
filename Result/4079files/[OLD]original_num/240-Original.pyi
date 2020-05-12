# (generated with --quick)

from typing import Any
import unittest.case

bowtie2_align: Any
bowtie2_build: Any
hash_file: Any
os: module
pkg_resources: module
read_checksums: Any
shutil: module
tempfile: module
unittest: module

class TestBowtie(unittest.case.TestCase):
    checksums: Any
    temp_dir: tempfile.TemporaryDirectory[nothing]
    def test_bowtie2_align(self) -> None: ...
    def test_bowtie2_build(self) -> None: ...
    def test_bowtie2_path(self) -> None: ...
