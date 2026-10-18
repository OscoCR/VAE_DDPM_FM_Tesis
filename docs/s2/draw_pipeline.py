"""Block diagram of the experimental pipeline: factors on the VAE, then the latent goes to DDPM and Flow Matching."""
from PIL import Image, ImageDraw, ImageFont
H = "/System/Library/Fonts/Helvetica.ttc"
F = lambda s, i=0: ImageFont.truetype(H, s, index=i)
INK, MUT = (40, 40, 40), (115, 115, 115)
C = {"data": (186, 214, 235), "vae": (203, 228, 207), "lat": (245, 211, 168), "gen": (214, 200, 230), "met": (231, 224, 196), "fac": (250, 244, 232)}
W, HT = 1850, 980
im = Image.new("RGB", (W, HT), (255, 255, 255)); d = ImageDraw.Draw(im)
def box(x, y, w, h, lines, fill, bold=0, outline=INK, fs=27):
    d.rounded_rectangle([x, y, x + w, y + h], radius=18, fill=fill, outline=outline, width=2)
    fonts = [F(fs, 1 if i < bold else 0) for i in range(len(lines))]
    tot = sum(f.size + 8 for f in fonts) - 8; cy = y + (h - tot) / 2
    for t, f in zip(lines, fonts):
        d.text((x + (w - d.textlength(t, font=f)) / 2, cy), t, fill=INK, font=f); cy += f.size + 8
def arr(x1, y1, x2, y2, col=INK):
    d.line([x1, y1, x2, y2], fill=col, width=3)
    if y1 == y2: d.polygon([(x2, y2), (x2 - 18, y2 - 10), (x2 - 18, y2 + 10)], fill=col)
    else: d.polygon([(x2, y2), (x2 - 10, y2 - 18), (x2 + 10, y2 - 18)], fill=col)
def dash(x1, y1, x2, y2, col=MUT):
    for x in range(x1, x2, 16): d.line([x, y1, min(x + 8, x2), y1], fill=col, width=2); d.line([x, y2, min(x + 8, x2), y2], fill=col, width=2)
    for y in range(y1, y2, 16): d.line([x1, y, x1, min(y + 8, y2)], fill=col, width=2); d.line([x2, y, x2, min(y + 8, y2)], fill=col, width=2)
# factors panel
d.rounded_rectangle([60, 30, 1790, 185], radius=22, fill=C["fac"], outline=(190, 180, 160), width=2)
d.text((90, 42), "Factors varied on the VAE (fractional factorial design, 16 cells)", fill=INK, font=F(29, 1))
tags = [("A", "Augmentation"), ("B", "Masking"), ("C", "Image selection"), ("D", "Modality: RGB or RGB-D"), ("E", "Variational layer"), ("F", "GAN")]
x = 90
for k, v in tags:
    w = int(d.textlength(v, font=F(25))) + 90
    d.rounded_rectangle([x, 100, x + w, 160], radius=16, fill=(255, 255, 255), outline=(190, 180, 160), width=2)
    d.text((x + 16, 114), k, fill=(150, 90, 40), font=F(28, 1)); d.text((x + 52, 117), v, fill=INK, font=F(25)); x += w + 22
# row 1: autoencoder
d.text((60, 200), "Stage 1: autoencoder (trained from scratch in every cell)", fill=MUT, font=F(26, 1))
box(60, 270, 260, 130, ["Training crop", "256×256", "RGB or RGB-D"], C["data"], 1)
box(400, 270, 220, 130, ["Encoder"], C["vae"], 1)
box(710, 270, 280, 130, ["Latent z", "4×32×32"], C["lat"], 1)
box(1080, 270, 220, 130, ["Decoder"], C["vae"], 1)
box(1390, 270, 400, 130, ["Reconstruction", "PSNR, SSIM, FID"], C["met"], 1)
dash(375, 245, 1325, 425)
arr(320, 335, 400, 335); arr(620, 335, 710, 335); arr(990, 335, 1080, 335); arr(1300, 335, 1390, 335)
arr(850, 185, 850, 245)
# row 2: generators
d.text((60, 480), "Stage 2: generators on the latents (DDPM and Flow Matching)", fill=MUT, font=F(26, 1))
arr(850, 400, 850, 540)
d.line([850, 540, 850, 540], fill=INK)
box(520, 560, 330, 120, ["DDPM", "1000 steps"], C["gen"], 1)
box(900, 560, 400, 120, ["Flow Matching", "50 Euler steps"], C["gen"], 1)
d.line([850, 520, 850, 540], fill=INK, width=3)
d.line([685, 540, 1100, 540], fill=INK, width=3)
arr(685, 540, 685, 560); arr(1100, 540, 1100, 560)
d.line([850, 400, 850, 520], fill=INK, width=3)
d.text((880, 440), "latents of the training set", fill=MUT, font=F(23))
# generation path
d.text((60, 720), "Generation", fill=MUT, font=F(26, 1))
box(60, 770, 260, 120, ["Noise", "4×32×32"], C["data"], 1)
box(430, 770, 360, 120, ["Generator", "DDPM or Flow Matching"], C["gen"], 1, fs=25)
box(900, 770, 320, 120, ["Decoder", "mean of the output"], C["vae"], 1, fs=25)
box(1330, 770, 460, 120, ["Generated images", "FID and KID against real images"], C["met"], 1, fs=25)
arr(320, 830, 430, 830); arr(790, 830, 900, 830); arr(1220, 830, 1330, 830)
d.line([685, 680, 685, 735], fill=MUT, width=2); d.line([1100, 680, 1100, 735], fill=MUT, width=2); d.line([685, 735, 1100, 735], fill=MUT, width=2)
d.line([610, 735, 610, 770], fill=MUT, width=2); d.line([610, 735, 685, 735], fill=MUT, width=2); arr(610, 735, 610, 770, MUT)
d.text((60, 925), "Every cell of the design yields one VAE and one DDPM; the factors that matter are repeated with Flow Matching.", fill=MUT, font=F(23))
im.save("Imagenes/pipeline_diagram.png", dpi=(200, 200)); im.save("docs/pipeline_diagram.png", dpi=(200, 200)); print("ok", im.size)
