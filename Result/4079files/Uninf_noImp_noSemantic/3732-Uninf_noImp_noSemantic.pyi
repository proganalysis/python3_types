import unittest
from typing import Any

class test_core(unittest.TestCase):
    portrait_pdf: Any = ...
    landscape_pdf: Any = ...
    def setUp(self) -> None: ...
    pages: Any = ...
    def tearDown(self) -> None: ...
    def test_reverse_remainder(self) -> None: ...
    def test_calculate_signature(self) -> None: ...
    def test_cut_in_signatures(self) -> None: ...
    def test_calculate_scaled_sub_page_size(self) -> None: ...
    def test_add_blanks(self) -> None: ...
    def test_get_media_box_size(self) -> None: ...
    def test_calculate_margins(self) -> None: ...
    def test_resize(self) -> None: ...
    def test_is_landscape(self) -> None: ...
    def test_validate_infile(self) -> None: ...
    def test_validate_papersize(self) -> None: ...
    def test_validate_pages_per_sheet(self) -> None: ...
    def test_validate_signature_length(self) -> None: ...
    def test_create_filename(self) -> None: ...
    def test_add_divider(self) -> None: ...
