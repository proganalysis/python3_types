#! /usr/bin/python3.5
# Copyright 2015 Chris Ballinger - CC0 1.0 Universal

import sys

# Octal / Emoji / Syllable Mapping
# `0	|	🌞	| ohm`
# `1	|	🌵	| ma`
# `2	|	🌲	| ni`
# `3	|	🌼	| pad`
# `4	|	🐅	| me`
# `5	|	🕊	| hum`
# `6	|	🐉	| free`
# `7	|	🌅	| dom`


# Input octal UTF-8 string (e.g. '012345670123456701234567') and receive
# an emoji representation.
def eyes_v01(o_string: str) -> str:
    o_string = o_string.replace('0', '🌞')
    o_string = o_string.replace('1', '🌵')
    o_string = o_string.replace('2', '🌲')
    o_string = o_string.replace('3', '🌼')
    o_string = o_string.replace('4', '🐅')
    o_string = o_string.replace('5', '🕊')
    o_string = o_string.replace('6', '🐉')
    o_string = o_string.replace('7', '🌅')
    return o_string


# Input octal UTF-8 string (e.g. '012345670123456701234567') and receive
# an pronounceable syllable representation.
def ears_v01(o_string: str) -> str:
    o_string = o_string.replace('0', 'ohm')
    o_string = o_string.replace('1', 'ma')
    o_string = o_string.replace('2', 'ni')
    o_string = o_string.replace('3', 'pad')
    o_string = o_string.replace('4', 'me')
    o_string = o_string.replace('5', 'hum')
    o_string = o_string.replace('6', 'free')
    o_string = o_string.replace('7', 'dom')
    return o_string

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('speakkey - v0.1\n\nUsage: speakkey.py "01234567 01234567 01234567" (octal only)')
    else:
        input_string = sys.argv[1]

        print('Eyes v0.1: ' + input_string)
        eyes = eyes_v01(input_string)
        print('         : ' + eyes)

        print('Ears v0.1: ' + input_string)
        ears = ears_v01(input_string)
        print('         : ' + ears)
