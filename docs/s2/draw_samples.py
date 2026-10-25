"""Figures of reconstructions and generated samples for Chapter V. Inputs are small samples copied from the cluster
(fixed positions, not selected by quality). Run from the repository root: python3 docs/s2/draw_samples.py SRC_DIR"""
import sys
from PIL import Image, ImageDraw, ImageFont
H = "/System/Library/Fonts/Helvetica.ttc"
F = lambda s, i=0: ImageFont.truetype(H, s, index=i)
SRC = sys.argv[1]
T, G, INK = 256, 8, (45, 45, 45)

def tile_grid(rows, col_titles, row_titles, left, out):
    ncol = len(rows[0]); nrow = len(rows)
    top = 70 if col_titles else 20
    W = left + ncol * (T + G) + 12; Hh = top + nrow * (T + G) + 12
    im = Image.new("RGB", (W, Hh), (255, 255, 255)); d = ImageDraw.Draw(im)
    for c, t in enumerate(col_titles or []):
        lines = t.split("\n")
        for k, ln in enumerate(lines):
            d.text((left + c * (T + G) + (T - d.textlength(ln, font=F(21))) / 2, 6 + k * 26), ln, fill=INK, font=F(21))
    for r, row in enumerate(rows):
        y = top + r * (T + G)
        if row_titles:
            lines = row_titles[r].split("\n")
            for k, ln in enumerate(lines):
                d.text((10, y + T / 2 - 14 * len(lines) + k * 28), ln, fill=INK, font=F(23))
        for c, f in enumerate(row):
            im.paste(Image.open(f).convert("RGB").resize((T, T)), (left + c * (T + G), y))
    im.save(out, dpi=(200, 200)); print(out, im.size)

idx = ["00000", "00090", "00180", "00270"]
rows = [[f"{SRC}/recon/{p}_{i}.png" for p in ("orig", "rgb", "rgbd", "gan")] for i in idx]
tile_grid(rows, ["Original", "VAE, RGB only\n(base repository)", "VAE, RGB-D", "VAE, RGB-D, adversarial\nloss, variational layer"], None, 12, "Imagenes/recon_comparison.png")

real = ["00000", "00060", "00120", "00180", "00240", "00300"]; gen = ["00000", "00001", "00002", "00003", "00004", "00005"]
rows = [[f"{SRC}/gen/real_{i}.png" for i in real], [f"{SRC}/gen/ddpm_{i}.png" for i in gen], [f"{SRC}/gen/fm_{i}.png" for i in gen]]
tile_grid(rows, None, ["Real\n(test)", "DDPM", "FM"], 120, "Imagenes/generated_samples.png")
