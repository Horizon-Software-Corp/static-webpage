from PIL import Image
import numpy as np


def make_opaque_pixels_white(src_path: str, dst_path: str) -> None:
    img = Image.open(src_path).convert("RGBA")

    # ★ copy() をつけて書き込み可能な配列を取得
    data = np.asarray(img, dtype=np.uint8).copy()
    # あるいは np.array(img, dtype=np.uint8) でも OK

    alpha = data[:, :, 3]
    mask = alpha > 0
    data[mask, 0:3] = 255     # ← ここで問題なく書き換えられる

    Image.fromarray(data, "RGBA").save(dst_path, optimize=True)


if __name__ == "__main__":
    make_opaque_pixels_white(
        "/home/n22/static-webpage/img/hero_logo_white.png",
        "/home/n22/static-webpage/img/hero_logo_white_white.png",
    )
