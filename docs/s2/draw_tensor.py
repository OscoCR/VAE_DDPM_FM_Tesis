"""Figure for section 2.2.1: a real crop of the dataset as a tensor and its latent (schematic).
Inputs: orig_00000.png (RGB crop) and depth_00000.png (estimated depth), copied from the cluster.
Run from the repository root: python3 docs/s2/draw_tensor.py SRC_DIR
Output: Imagenes/pixels_to_tensors.png"""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

H = "/System/Library/Fonts/Helvetica.ttc"
F = lambda s, i=0: ImageFont.truetype(H, s, index=i)
INK, MUT, RED = (45, 45, 45), (110, 110, 110), (200, 50, 50)
SRC = sys.argv[1]
rgb = Image.open(f"{SRC}/orig_00000.png").convert("RGB")
dep = Image.open(f"{SRC}/depth_00000.png").convert("L")
a = np.array(rgb)
PY, PX = 70, 124                      # 6x6 patch of the green channel
patch = a[PY:PY + 6, PX:PX + 6, 1]

W, Hh = 1960, 560
im = Image.new("RGB", (W, Hh), (255, 255, 255))
d = ImageDraw.Draw(im)

def txt(x, y, s, f=24, fill=INK, center=False):
    if center:
        x -= d.textlength(s, font=F(f)) / 2
    d.text((x, y), s, fill=fill, font=F(f))

def arrow(x1, y, x2, label=None):
    d.line([x1, y, x2 - 14, y], fill=INK, width=4)
    d.polygon([(x2, y), (x2 - 18, y - 10), (x2 - 18, y + 10)], fill=INK)
    if label:
        txt((x1 + x2) / 2, y - 40, label, 22, MUT, center=True)

# 1) the crop
S1 = 300
txt(40, 24, "A crop of the dataset", 28)
im.paste(rgb.resize((S1, S1), Image.LANCZOS), (40, 80))
k = S1 / 256
bx, by = 40 + PX * k, 80 + PY * k
d.rectangle([bx - 6, by - 6, bx + 6 * k + 6, by + 6 * k + 6], outline=RED, width=3)
txt(40, 80 + S1 + 14, "256 x 256 pixels, as stored", 22, MUT)

# 2) the four channels
arrow(360, 80 + S1 / 2, 430)
S2, gx, gy = 170, 450, 80
labels = ["R", "G", "B", "Depth (estimated)"]
chans = [Image.fromarray(a[..., c]) for c in range(3)] + [dep]
for i, (lab, ch) in enumerate(zip(labels, chans)):
    x = gx + (i % 2) * (S2 + 18)
    y = gy + (i // 2) * (S2 + 56)
    im.paste(ch.resize((S2, S2), Image.LANCZOS).convert("RGB"), (x, y))
    txt(x, y + S2 + 6, lab, 22, INK)
    if lab == "G":
        kk = S2 / 256
        d.rectangle([x + PX * kk - 3, y + PY * kk - 3, x + (PX + 6) * kk + 3, y + (PY + 6) * kk + 3], outline=RED, width=2)
txt(gx, gy + 2 * (S2 + 56) - 6, "one channel = one grid of numbers", 22, MUT)

# 3) the numbers of a patch
nx, ny = 880, 110
txt(nx - 6, 24, "Each pixel is a number", 28)
cell = 66
for r in range(6):
    for c in range(6):
        x, y = nx + c * cell, ny + 20 + r * cell * 0.62
        v = int(patch[r, c])
        d.rectangle([x, y, x + cell, y + cell * 0.62], outline=(190, 190, 190), width=1,
                    fill=(int(v), int(v), int(v)) if False else (255, 255, 255))
        txt(x + cell / 2, y + 12, str(v), 22, INK, center=True)
txt(nx, ny + 20 + 6 * cell * 0.62 + 12, "6 x 6 pixels of the green channel (0 to 255)", 22, MUT)
txt(nx, ny + 20 + 6 * cell * 0.62 + 44, "divided by 255, every value lies in [0, 1]", 22, MUT)

# 4) the tensor
arrow(1310, 230, 1390)
tx, ty, ts = 1415, 120, 150
for i in range(3, -1, -1):
    ox, oy = i * 16, -i * 16
    col = [(255, 235, 235), (235, 245, 235), (235, 235, 255), (240, 240, 240)][i]
    d.rectangle([tx + ox, ty + oy + 40, tx + ox + ts, ty + oy + 40 + ts], fill=col, outline=INK, width=2)
txt(tx - 10, ty + 40 + ts + 24, "tensor (4, 256, 256)", 24)
txt(tx - 10, ty + 40 + ts + 56, "262,144 numbers", 22, MUT)
txt(tx - 10, ty + 40 + ts + 84, "(R, G, B, depth)", 22, MUT)

# 5) the latent (schematic)
arrow(1630, 230, 1730, "encoder")
lx, ly, ls = 1765, 190, 46
for i in range(3, -1, -1):
    ox, oy = i * 8, -i * 8
    d.rectangle([lx + ox, ly + oy, lx + ox + ls, ly + oy + ls], fill=(250, 245, 225), outline=INK, width=2)
txt(1745, ly + ls + 28, "latent (4, 32, 32)", 20, INK)
txt(1745, ly + ls + 56, "4,096 numbers", 20, MUT)
txt(1745, ly + ls + 82, "64 times fewer", 20, MUT)
txt(1745, ly + ls + 112, "(schematic)", 20, MUT)

im.save("Imagenes/pixels_to_tensors.png", dpi=(200, 200))
print("ok", im.size)
