# -*- coding: utf-8 -*-

import struct


def write_int8(octet: bytes, pos: int, value: int):
    octet = bytearray(octet)
    octet[pos] = value
    return bytes(octet)


def write_int16(octet: bytes, pos: int, value: int, big_endian: bool = False):
    octet = bytearray(octet)
    if big_endian:
        octet[pos] = value >> 8
        octet[pos + 1] = value & 0x00FF
    else:
        octet[pos + 1] = value >> 8
        octet[pos] = value & 0x00FF
    return bytes(octet)


def write_int24(octet: bytes, pos: int, value: int, big_endian: bool = False):
    octet = bytearray(octet)
    if big_endian:
        octet[pos] = value >> 16
        octet[pos + 1] = value >> 8 & 0x0000FF
        octet[pos + 2] = value & 0x0000FF
    else:
        octet[pos + 2] = value >> 16
        octet[pos + 1] = value >> 8 & 0x0000FF
        octet[pos] = value & 0x0000FF
    return bytes(octet)


def write_int32(octet: bytes, pos: int, value: int, big_endian: bool = False):
    octet = bytearray(octet)
    if big_endian:
        octet[pos] = value >> 24
        octet[pos + 1] = value >> 16 & 0x0000FF
        octet[pos + 2] = value >> 8 & 0x0000FF
        octet[pos + 3] = value & 0x000000FF
    else:
        octet[pos + 3] = value >> 24
        octet[pos + 2] = value >> 16 & 0x0000FF
        octet[pos + 1] = value >> 8 & 0x0000FF
        octet[pos] = value & 0x000000FF
    return bytes(octet)


def write_str(octet: bytes, pos: int, length: int, value: str, big_endian: bool = False):
    octet = bytearray(octet)
    if big_endian:
        for i in range(length):
            octet[pos + length - i - 1] = value[i]
    else:
        for i in range(length):
            octet[pos + i] = value[i]
    return bytes(octet)
