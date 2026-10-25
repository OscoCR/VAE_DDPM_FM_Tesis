"""Gantt chart of the workplan by calendar month, November 2026 to October 2027. Run from the repository root.
Output: Imagenes/gantt_workplan.png and docs/gantt_workplan.png"""
from PIL import Image, ImageDraw, ImageFont
H = "/System/Library/Fonts/Helvetica.ttc"
F = lambda s, i=0: ImageFont.truetype(H, s, index=i)
INK, MUT, GRID = (45, 45, 45), (120, 120, 120), (232, 232, 228)
PAL = {"code": (186, 214, 235), "s0": (203, 228, 207), "s1": (160, 205, 170), "an": (231, 224, 196),
       "s2": (245, 211, 168), "s3": (240, 190, 160), "pap": (214, 200, 230), "wr": (200, 205, 215), "opt": (240, 240, 236)}
MONTHS = ["Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
# (name, start, end, color key, soft, label); start and end in months counted from 1 November 2026
ROWS = [("Proposal and corrections", 0, 3, "an", False, "Nov–Jan"),
        ("Code and infrastructure", 3, 5, "code", False, "Feb–Mar"),
        ("Stage 0: noise, convergence, N", 5, 6, "s0", False, "Apr"),
        ("Stage 1: screening (DDPM)", 6, 8, "s1", False, "May–Jun", "room for up to five replicates"),
        ("Analysis of Stage 1", 8, 8.6, "an", False, "Jul"),
        ("Stage 2: refinement", 8.6, 9.6, "s2", False, "Jul–Aug"),
        ("Stage 3: confirmation (FM)", 9.6, 10.4, "s3", False, "Aug–Sep", ""),
        ("Final analysis and thesis", 10.2, 12, "wr", False, "Sep–Oct"),
        ("Paper and thesis drafting (parallel)", 3, 11, "wr", True, "from February, results added as they appear"),
        ("DINO extension (optional)", 8.6, 10.6, "opt", True, "Jul–Sep"),
        ("Osnabrück stay (optional, one month)", 5, 11, "opt", True, "one month, date to be set (April to September)")]
ROWS = [r if len(r) == 7 else r + ("",) for r in ROWS]
W, LEFT, TOP, RH = 1700, 560, 165, 66
MW = (W - LEFT - 40) / 12
HGT = TOP + RH * len(ROWS) + 90
im = Image.new("RGB", (W, HGT), (255, 255, 255)); d = ImageDraw.Draw(im)
d.text((40, 18), "Workplan by month, November 2026 to October 2027", fill=INK, font=F(34, 1))
for m in range(13):
    x = LEFT + m * MW
    d.line([x, TOP - 8, x, TOP + RH * len(ROWS)], fill=GRID, width=1)
for m, name in enumerate(MONTHS):
    x = LEFT + m * MW
    d.text((x + MW / 2 - d.textlength(name, font=F(22)) / 2, TOP - 42), name, fill=MUT, font=F(22))
d.text((LEFT + 0.2 * MW, TOP - 80), "2026", fill=MUT, font=F(20, 1))
d.text((LEFT + 2.2 * MW, TOP - 80), "2027", fill=MUT, font=F(20, 1))
d.line([LEFT + 2 * MW, TOP - 80, LEFT + 2 * MW, TOP - 8], fill=(190, 190, 185), width=2)
for i, (name, a, b, key, soft, lab, note) in enumerate(ROWS):
    y = TOP + i * RH
    d.text((40, y + RH / 2 - 14), name, fill=INK if not soft else MUT, font=F(25))
    x1, x2 = LEFT + a * MW + 4, LEFT + b * MW - 4
    box = [x1, y + 12, x2, y + RH - 12]
    if soft:
        d.rounded_rectangle(box, radius=14, fill=(250, 250, 247) if key == "opt" else (232, 235, 240), outline=(170, 170, 165), width=2)
    else:
        d.rounded_rectangle(box, radius=14, fill=PAL[key])
    size = 20
    while d.textlength(lab, font=F(size)) > (x2 - x1) - 12 and size > 16:
        size -= 1
    f = F(size)
    if d.textlength(lab, font=f) > (x2 - x1) - 12:
        d.text((x2 + 10, y + RH / 2 - 12), lab, fill=INK if not soft else MUT, font=F(20))
    else:
        d.text(((x1 + x2) / 2 - d.textlength(lab, font=f) / 2, y + RH / 2 - size / 2 - 2), lab, fill=INK if not soft else MUT, font=f)
    if note:
        d.text((x2 + 12, y + RH / 2 - 11), note, fill=MUT, font=F(20))
d.text((40, TOP + RH * len(ROWS) + 30), "Filled bars: planned work. Pale bars with an outline: parallel or optional work. Thesis delivery about October 2027.", fill=MUT, font=F(22))
im.save("Imagenes/gantt_workplan.png", dpi=(200, 200)); im.save("docs/gantt_workplan.png", dpi=(200, 200)); print("ok", im.size)
