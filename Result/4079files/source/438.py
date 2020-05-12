"""
Roman Numerals
https://py.checkio.org/mission/roman-numerals/
"""


def checkio1(data):
    i = data
    result = ''

    result += "M" * int(i / 1000)
    i %= 1000
    result += "D" * int(i / 500)
    i %= 500

    if int(i / 100) == 9:
        result += 'CM'
    elif int(i / 100) == 4:
        result += 'CD'
    else:
        result += 'C' * int(i / 100)
    i %= 100

    if int(i / 10) == 9:
        result += 'XC'
    elif int(i / 10) == 4:
        result += 'XL'
    else:
        result += "L" * int(i / 50)
        i %= 50
        result += 'X' * int(i / 10)
    i %= 10

    if i == 9:
        result += 'IX'
    elif i == 4:
        result += 'IV'
    else:
        result += "V" * int(i / 5)
        i %= 5
        result += "I" * i

    return result


def checkio2(data):
    i = data
    result = ''
    result += "M" * int(i / 1000)
    i %= 1000
    result += "CM" * int(i / 900)
    i %= 900
    result += "D" * int(i / 500)
    i %= 500
    result += "CD" * int(i / 400)
    i %= 400
    result += 'C' * int(i / 100)
    i %= 100
    result += 'XC' * int(i / 90)
    i %= 90
    result += "L" * int(i / 50)
    i %= 50
    result += 'XL' * int(i / 40)
    i %= 40
    result += 'X' * int(i / 10)
    i %= 10
    result += 'IX' * int(i / 9)
    i %= 9
    result += "V" * int(i / 5)
    i %= 5
    result += "IV" * int(i / 4)
    i %= 4
    result += "I" * i

    return result


def checkio3(data):
    romans = (('M', 1000),
              ('CM', 900),
              ('D', 500),
              ('CD', 400),
              ('C', 100),
              ('XC', 90),
              ('L', 50),
              ('XL', 40),
              ('X', 10),
              ('IX', 9),
              ('V', 5),
              ('IV', 4),
              ('I', 1))
    i = data
    result = ''
    for r in romans:
        result += r[0] * int(i / r[1])
        i %= r[1]
    return result


if __name__ == '__main__':
    assert checkio1(6) == 'VI', '6'
    assert checkio1(76) == 'LXXVI', '76'
    assert checkio1(499) == 'CDXCIX', '499'
    assert checkio1(3888) == 'MMMDCCCLXXXVIII', '3888'
    assert checkio2(6) == 'VI', '6'
    assert checkio2(76) == 'LXXVI', '76'
    assert checkio2(499) == 'CDXCIX', '499'
    assert checkio2(3888) == 'MMMDCCCLXXXVIII', '3888'
    assert checkio3(6) == 'VI', '6'
    assert checkio3(76) == 'LXXVI', '76'
    assert checkio3(499) == 'CDXCIX', '499'
    assert checkio3(3888) == 'MMMDCCCLXXXVIII', '3888'
