import pytest

from chandere.errors import ChandereError
from chandere.loader import load_scraper

scraper = load_scraper("4chan")

VALID_CROSSLINK_TARGETS = [
    ("/c/1990691", ("c", "1990691")),
    ("/c/ 1990691", ("c", "1990691")),
    ("c/1990691", ("c", "1990691")),
    ("/c 1990691", ("c", "1990691")),
    ("c 1990691", ("c", "1990691")),
    ("/c/", ("c", None)),
    ("/c", ("c", None)),
    ("c/", ("c", None)),
    ("c", ("c", None)),
]

INVALID_CROSSLINK_TARGETS = [
    "/"
]

VALID_URI_TARGETS = [
    ("https://boards.4chan.org/c/thread/1990691/asdf", ("c", "1990691")),
    ("http://boards.4chan.org/c/thread/1990691/asdf", ("c", "1990691")),
    ("https://boards.4chan.org/c/thread/1990691/", ("c", "1990691")),
    ("http://boards.4chan.org/c/thread/1990691/", ("c", "1990691")),
    ("https://4chan.org/c/thread/1990691/asdf", ("c", "1990691")),
    ("http://4chan.org/c/thread/1990691/asdf", ("c", "1990691")),
    ("https://4chan.org/c/thread/1990691/", ("c", "1990691")),
    ("http://4chan.org/c/thread/1990691/", ("c", "1990691")),
    ("https://4chan.org/c/", ("c", None)),
    ("http://4chan.org/c/", ("c", None)),
]

INVALID_URI_TARGETS = [
    "https://4chan.org/",
    "http://4chan.org/",
    "https://google.com/",
    "http://google.com/"
]


def test_parse_valid_uri_target():
    for target, expected in VALID_URI_TARGETS:
        assert scraper.parse_target(target) == expected


def test_parse_invalid_uri_target():
    for target in INVALID_URI_TARGETS:
        with pytest.raises(ChandereError):
            scraper.parse_target(target)


def test_parse_valid_crosslink_target():
    for target, expected in VALID_CROSSLINK_TARGETS:
        assert scraper.parse_target(target) == expected


def test_parse_invalid_crosslink_target():
    for target in INVALID_CROSSLINK_TARGETS:
        with pytest.raises(ChandereError):
            scraper.parse_target(target)
