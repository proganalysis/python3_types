# (generated with --quick)

from typing import Any, Dict, List, TypeVar, Union

AbstractConsonant: Any
AbstractPosition: Any
BACK_TO_FRONT_VOWELS: Any
Backness: Any
Consonant: Any
DIPHTHONGS_IPA: Dict[str, str]
DIPHTHONGS_IPA_class: Dict[str, Any]
GEMINATE_CONSONANTS: Dict[str, str]
Height: Any
IPA: Dict[str, str]
IPA_class: Dict[str, Any]
Length: Any
Manner: Any
OLD_NORSE_PHONOLOGY: list
Place: Any
Rank: Any
Rule: Any
Vowel: Any
__author__: List[str]
a: Any
ao: Any
b: Any
d: Any
dh: Any
e: Any
ee: Any
f: Any
g: Any
gh: Any
h: Any
i: Any
j: Any
k: Any
l: Any
m: Any
n: Any
o: Any
oe: Any
oee: Any
old_norse_rules: list
oo: Any
p: Any
r: Any
rule_f: list
rule_g: list
rule_th: list
s: Any
t: Any
th: Any
u: Any
v: Any
y: Any

_T0 = TypeVar('_T0')

class OldNorsePhonology(Any):
    U_UMLAUT: Dict[str, str]
    @staticmethod
    def orthographic_i_umlaut(sound) -> Any: ...
    @staticmethod
    def orthographic_u_umlaut(sound: _T0) -> Union[str, _T0]: ...
    @staticmethod
    def phonetic_i_umlaut(sound) -> Any: ...
    @staticmethod
    def phonetic_u_umlaut(sound) -> Any: ...

def measure_old_norse_syllable(syllable) -> Any: ...
def normalize_for_syllabifier(text) -> Any: ...
