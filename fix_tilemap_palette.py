#!/usr/bin/env python3
import sys

TARGET_SLOT = 0xD

with open("graphics/title_screen/firered/box_art_mon.bin", "rb") as f:
    data = bytearray(f.read())

for i in range(0, len(data), 2):
    entry = data[i] | (data[i+1] << 8)
    tile_index = entry & 0x3FF
    flags = entry & 0xC00
    new_entry = tile_index | flags | (TARGET_SLOT << 12)
    data[i]   = new_entry & 0xFF
    data[i+1] = (new_entry >> 8) & 0xFF

with open("graphics/title_screen/firered/box_art_mon.bin", "wb") as f:
    f.write(data)

print(f"Done. {len(data)//2} entries patched to palette slot {TARGET_SLOT}.")
