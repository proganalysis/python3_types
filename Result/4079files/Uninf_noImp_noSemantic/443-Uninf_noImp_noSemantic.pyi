from cltk.phonology.utils import Length, Vowel
from typing import Any, Union

__author__: Any

class OldNorsePhonology(Vowel):
    U_UMLAUT: Any = ...
    @staticmethod
    def phonetic_i_umlaut(sound: Vowel) -> Vowel: ...
    @staticmethod
    def orthographic_i_umlaut(sound: str) -> str: ...
    @staticmethod
    def phonetic_u_umlaut(sound: Vowel) -> Vowel: ...
    @staticmethod
    def orthographic_u_umlaut(sound: str) -> str: ...

a: Any
ee: Any
e: Any
oee: Any
oe: Any
i: Any
y: Any
ao: Any
oo: Any
o: Any
u: Any
b: Any
d: Any
f: Any
g: Any
gh: Any
h: Any
j: Any
k: Any
l: Any
m: Any
n: Any
p: Any
r: Any
s: Any
t: Any
v: Any
th: Any
dh: Any
OLD_NORSE_PHONOLOGY: Any
DIPHTHONGS_IPA: Any
DIPHTHONGS_IPA_class: Any
IPA: Any
IPA_class: Any
GEMINATE_CONSONANTS: Any
rule_th: Any
rule_f: Any
rule_g: Any
old_norse_rules: Any

def measure_old_norse_syllable(syllable: list) -> Union[Length, None]: ...
def normalize_for_syllabifier(text: str) -> str: ...
