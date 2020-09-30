'''

Public api

'''
from typing import Set

from britfoner import Seq, _UNSTRESSED_BRITFONE, _MODEL_OUT
from britfoner.IO import all_encoded, bounded, dictionary_from, model_from, indexes_from
from britfoner.g2p import most_likely_sequence

# Length of the longest word in Britfone, the pronunciation dictionary
# A limitation of this model is that input/output sequences have a fixed length
# and need therefore be represented by the longest available sequence
MAX_LENGTH = 18

_dictionary  = dictionary_from(_UNSTRESSED_BRITFONE)

_letter_index, _inv_phone_index = indexes_from(_dictionary)

_model = model_from('20x32x256x19x48x1.h5')

_EMPTY_SET = set()


def pronounce(word: str) -> Set[Seq]:
    '''
    Gives British English pronunciation(s) of word as symbols in the International Phonetic Alphabet

    Strings longer than 18 characters are given no pronunciations

    *input is not validated*

    :param word: a non-empty String of length 18 at most, containing characters in [A-Za-z' ]
    :return: a set of string tuples representing the pronunciations of ``word``
    '''

    if len(word) > MAX_LENGTH: return _EMPTY_SET

    norm_word = tuple(word.upper())
    sounds = _dictionary.get(norm_word, None)

    if not sounds:
        bound_word = [bounded(norm_word, MAX_LENGTH)]
        y_hat = _model.predict([all_encoded(bound_word, _letter_index, reverse=True)])[0]
        sounds = {most_likely_sequence(y_hat, _inv_phone_index)}

    return sounds
