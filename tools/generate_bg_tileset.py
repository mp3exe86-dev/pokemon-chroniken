#!/usr/bin/env python3
"""
generate_bg_tileset.py - GBA 8bpp BG Tileset + Tilemap Generator

Converts a PNG image into a deduplicated GBA 8bpp tileset (.8bpp) and
a matching tilemap (.bin) for use as a background layer.

Usage: python3 tools/generate_bg_tileset.py <input.png> <output.8bpp> <output.bin>

Constraints:
- Input must be an indexed-color PNG (palette mode 'P')
- Maximum 256 unique 8x8 tiles (GBA 8bpp charBase limit)
- Image dimensions must be multiples of 8
- Tilemap covers 32 columns x 20 rows (GBA visible area, screenSize=0)

Output:
- <output.8bpp>: Deduplicated tile data, each tile 64 bytes (8x8 @ 8bpp)
- <output.bin>: Tilemap, 640 x uint16 entries (32x20 tile indices, little-endian)
"""

import sys
import struct
from PIL import Image


def extract_tile(pixels, tx, ty, img_width):
    """Extract an 8x8 tile as a bytes object from pixel data."""
    tile = []
    for row in range(8):
        y = ty * 8 + row
        for col in range(8):
            x = tx * 8 + col
            if x < img_width and y < len(pixels) // img_width:
                tile.append(pixels[y * img_width + x])
            else:
                tile.append(0)
    return bytes(tile)


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <input.png> <output.8bpp> <output.bin>")
        sys.exit(1)

    input_png = sys.argv[1]
    output_8bpp = sys.argv[2]
    output_bin = sys.argv[3]

    img = Image.open(input_png)

    if img.mode != 'P':
        print(f"ERROR: {input_png} must be an indexed-color PNG (mode 'P'), got '{img.mode}'")
        sys.exit(1)

    width, height = img.size

    if width % 8 != 0 or height % 8 != 0:
        print(f"ERROR: Image dimensions must be multiples of 8, got {width}x{height}")
        sys.exit(1)

    pixels = list(img.tobytes())
    tiles_x = width // 8
    tiles_y = height // 8

    # Deduplicate tiles
    unique_tiles = []
    tile_index_map = {}
    tilemap_entries = []

    for ty in range(tiles_y):
        for tx in range(tiles_x):
            tile = extract_tile(pixels, tx, ty, width)
            if tile not in tile_index_map:
                if len(unique_tiles) >= 256:
                    print(f"ERROR: Image has more than 256 unique 8x8 tiles "
                          f"(exceeded at tile {tx},{ty}). "
                          f"Reduce unique regions to fit GBA 8bpp charBase (16KB = 256 tiles max).")
                    sys.exit(1)
                tile_index_map[tile] = len(unique_tiles)
                unique_tiles.append(tile)
            tilemap_entries.append(tile_index_map[tile])

    # Build tilemap: 32 columns x 20 rows (GBA screenSize=0 visible area)
    # Pad or crop to exactly 32x20 entries
    MAP_COLS = 32
    MAP_ROWS = 20
    tilemap = []
    for row in range(MAP_ROWS):
        for col in range(MAP_COLS):
            if row < tiles_y and col < tiles_x:
                src_idx = row * tiles_x + col
                tilemap.append(tilemap_entries[src_idx])
            else:
                tilemap.append(0)

    # Write deduplicated tileset
    with open(output_8bpp, 'wb') as f:
        for tile in unique_tiles:
            f.write(tile)

    # Write tilemap (640 x uint16, little-endian)
    with open(output_bin, 'wb') as f:
        f.write(struct.pack(f'<{MAP_COLS * MAP_ROWS}H', *tilemap))

    print(f"generate_bg_tileset: {input_png} -> {len(unique_tiles)} unique tiles, "
          f"{MAP_COLS}x{MAP_ROWS} tilemap")


if __name__ == '__main__':
    main()
