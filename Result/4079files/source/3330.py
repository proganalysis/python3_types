# -*- coding: utf-8 -*-


def read_rom(rom_path: str):
    with open(rom_path, mode='rb') as bios:
        print('Reading and loading "', rom_path, '" bios file into memory ...')
        return bios.read()
