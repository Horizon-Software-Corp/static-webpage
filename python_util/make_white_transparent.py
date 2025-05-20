#!/usr/bin/env python3
"""
白～淡いグレーまで透過（α=0）に置き換えるスクリプト

使い方:
    python make_whiteish_transparent.py \
        /path/to/input.png /path/to/output.png  --th 230 --diff 25
"""
import sys
from pathlib import Path
from PIL import Image
import argparse


def whiteish_to_alpha(src: Path, dst: Path, th: int = 10, diff: int = 121):
    """
    - th   : 明るさしきい値 (0-255)。RGB 各値が th 以上なら“十分明るい”とみなす
    - diff : RGB チャンネル間の最大差。色味が強い場合に透過し過ぎるのを防ぐ
    """
    img = Image.open(src).convert("RGBA")
    pixels = img.load()

    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if (
                r >= th and g >= th and b >= th           # 明るい
                and max(r, g, b) - min(r, g, b) <= diff  # 色味が薄い
            ):
                pixels[x, y] = (255, 255, 255, 0)  # 完全透過
    img.save(dst, "PNG")
    print(f"✅ saved: {dst}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="make (almost) white transparent")
    parser.add_argument("src")
    parser.add_argument("dst")
    parser.add_argument("--th", type=int, default=230,
                        help="brightness threshold (default 230)")
    parser.add_argument("--diff", type=int, default=25,
                        help="max RGB channel difference (default 25)")
    args = parser.parse_args()

    whiteish_to_alpha(Path(args.src), Path(args.dst), args.th, args.diff)
