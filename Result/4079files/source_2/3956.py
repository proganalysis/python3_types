# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from future.builtins import bytes
import random
import unicodedata


def sample_bytes(length=100, seed=1):
    """
    Generate pseudo-random deterministic byte-messages for testing

    :param int length: Number of bytes to return
    :param int seed: Seed used to initialize random byte generator
    :return bytearray: `bytearray` of size length
    """
    # Lock-in to give the same pseudo-random data with function call
    random.seed(seed)
    return bytes([random.getrandbits(8) for _ in range(length)])


def normalize_text(text):
    """
    Removes diacritics, punctuation and other messy stuff from strings and
    normalizes separators.

    Note: Simple transliteration to ASCII characters is not an option as
    it would eliminate languages like Greek, Russian and many othes.

    :param str|unicode text:
    :return str|unicode: normalized text
    """

    #: Letter and Number unicode categories
    whitelist = 'LNS'
    #: Canonical decomposition, so we catch diacritics separately
    decomposed = unicodedata.normalize('NFD', text)

    chars = []
    for char in decomposed:
        cat = unicodedata.category(char)
        # normalize seperators
        if cat.startswith(u'Z'):
            chars.append(u' ')
        # filter crazy stuff
        elif cat[0] in whitelist:
            chars.append(char.lower())
    filtered = u''.join(chars)

    # Remove leading, trailing and duplicate seperators
    collapsed = u' '.join(filtered.split())

    # Build canonical composition
    normalized = unicodedata.normalize('NFC', collapsed)

    return normalized
