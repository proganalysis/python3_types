import unittest
from typing import Union


class Prostokat:
    def __init__(self, bok_a: Union[float, int], bok_b: [float, int]) -> None:
        if not isinstance(bok_a, (float, int)) or bok_a <= 0:
            raise ValueError('Długość boku A musi być więszka od 0')

        if not isinstance(bok_b, (float, int)) or bok_b <= 0:
            raise ValueError('Długość boku B musi być więszka od 0')

        self.bok_a = float(bok_a)
        self.bok_b = float(bok_b)

    def pole(self) -> float:
        return self.bok_a * self.bok_b

    def obwod(self) -> float:
        return 2 * (self.bok_a+self.bok_b)

    def __str__(self) -> str:
        return f'Prostokat(a={self.bok_a}, b={self.bok_b})'


class ProstokatTest(unittest.TestCase):

    def setUp(self):
        self.prostokat = Prostokat(bok_a=10, bok_b=20)

    def test_poprawnego_tworzenie_prostokata(self):
        Prostokat(bok_a=5, bok_b=10)

    def test_prostokata_bok_nieprawidlowy(self):
        with self.assertRaises(ValueError):
            Prostokat(bok_a='a', bok_b=20)

        with self.assertRaises(ValueError):
            Prostokat(bok_a=20, bok_b='b')

        with self.assertRaises(ValueError):
            Prostokat(bok_a='b', bok_b='b')

    def test_prostokata_bok_zero(self):
        with self.assertRaises(ValueError):
            Prostokat(bok_a=0, bok_b=20)

        with self.assertRaises(ValueError):
            Prostokat(bok_a=20, bok_b=0)

        with self.assertRaises(ValueError):
            Prostokat(bok_a=0, bok_b=0)

    def test_prostokata_bok_ujemny(self):
        with self.assertRaises(ValueError):
            Prostokat(bok_a=-3, bok_b=20)

        with self.assertRaises(ValueError):
            Prostokat(bok_a=20, bok_b=-3)

        with self.assertRaises(ValueError):
            Prostokat(bok_a=-1, bok_b=-3)

    def test_ustawienia_jednego_boku(self):
        with self.assertRaises(TypeError):
            Prostokat(bok_a=0)

        with self.assertRaises(TypeError):
            Prostokat(bok_b=0)

    def test_przechowywanie_wartosci(self):
        p = Prostokat(bok_a=5, bok_b=10)
        self.assertEqual(p.bok_a, 5)
        self.assertEqual(p.bok_b, 10)

    def test_tworzenie_prostokata(self):
        self.assertEqual(self.prostokat.bok_a, 10)
        self.assertEqual(self.prostokat.bok_b, 20)

    def test_pola(self):
        self.assertEqual(self.prostokat.pole(), 200.0)

    def test_obwod(self):
        self.assertEqual(self.prostokat.obwod(), 60)

    def test_prostokat_to_string(self):
        self.assertEqual(str(self.prostokat), 'Prostokat(a=10.0, b=20.0)')


if __name__ == '__main__':
    unittest.main()
