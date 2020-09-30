# -*- coding: utf-8 -*-


def write_rom(rom_path: str, rom_content: bytes):
    with open(rom_path, mode='wb') as bios:
        print('Writing "', rom_path, '" bios file ...')
        return bios.write(rom_content)
