"""Soft Gantt chart of the workplan (weeks, no calendar dates). Output: Imagenes/gantt_workplan.png"""
from PIL import Image, ImageDraw, ImageFont
H = "/System/Library/Fonts/Helvetica.ttc"
F = lambda s, i=0: ImageFont.truetype(H, s, index=i)
INK, MUT, GRID = (45, 45, 45), (120, 120, 120), (232, 232, 228)
PAL = {"code": (186, 214, 235), "s0": (203, 228, 207), "s1": (160, 205, 170), "an": (231, 224, 196),
       "s2": (245, 211, 168), "s3": (240, 190, 160), "pap": (214, 200, 230), "wr": (200, 205, 215), "opt": (240, 240, 236)}
ROWS = [("Code and infrastructure", 1, 3, "code", False), ("Stage 0: noise and convergence", 4, 5, "s0", False),
        ("Stage 1: screening (DDPM)", 6, 10, "s1", False), ("Analysis of Stage 1", 11, 12, "an", False),
        ("Stage 2: refinement", 13, 15, "s2", False), ("Stage 3: confirmation (Flow Matching)", 16, 17, "s3", False),
        ("Final analysis and paper", 18, 21, "pap", False), ("Thesis writing", 22, 26, "wr", False),
        ("Drafting in parallel", 6, 21, "wr", True), ("DINO extension (optional)", 11, 17, "opt", True),
        ("Osnabrück exchange (optional)", 18, 21, "opt", True)]
W, LEFT, TOP, RH, WK = 1700, 520, 120, 66, 44
HGT = TOP + RH * len(ROWS) + 90
im = Image.new("RGB", (W, HGT), (255, 255, 255)); d = ImageDraw.Draw(im)
d.text((40, 28), "Workplan (estimated weeks)", fill=INK, font=F(34, 1))
for w in range(1, 27):
    x = LEFT + (w - 1) * WK
    d.line([x, TOP - 8, x, TOP + RH * len(ROWS)], fill=GRID, width=1)
    if w == 1 or w % 2 == 0:
        t = str(w); d.text((x + WK / 2 - d.textlength(t, font=F(22)) / 2, TOP - 42), t, fill=MUT, font=F(22))
d.line([LEFT + 26 * WK, TOP - 8, LEFT + 26 * WK, TOP + RH * len(ROWS)], fill=GRID, width=1)
for i, (name, a, b, key, soft) in enumerate(ROWS):
    y = TOP + i * RH
    d.text((40, y + RH / 2 - 14), name, fill=INK if not soft else MUT, font=F(25))
    x1, x2 = LEFT + (a - 1) * WK + 4, LEFT + b * WK - 4
    box = [x1, y + 12, x2, y + RH - 12]
    if soft:
        d.rounded_rectangle(box, radius=14, fill=(250, 250, 247) if key == "opt" else (232, 235, 240), outline=(170, 170, 165), width=2)
    else:
        d.rounded_rectangle(box, radius=14, fill=PAL[key])
    lab = f"{a}–{b}"; d.text(((x1 + x2) / 2 - d.textlength(lab, font=F(20)) / 2, y + RH / 2 - 12), lab, fill=INK if not soft else MUT, font=F(20))
d.text((40, TOP + RH * len(ROWS) + 30), "Filled bars: planned work. Pale bars with an outline: parallel or optional work. About 26 weeks, six months.", fill=MUT, font=F(22))
im.save("Imagenes/gantt_workplan.png", dpi=(200, 200)); im.save("docs/gantt_workplan.png", dpi=(200, 200)); print("ok", im.size)
