"""Two-source PRISMA 2020-style flow diagram (arXiv 11-Oct-2026 + Semantic Scholar 18-Oct-2026). Numbers from docs/s2/prisma_combined_numbers.json."""
import json
from PIL import Image, ImageDraw, ImageFont
N = json.load(open("docs/s2/prisma_combined_numbers.json"))
arx_rec, s2_rec = 166, 276                      # sum of the five strings per source (30+73+9+47+7, 48+123+18+79+8)
dup_in, dup_between = (arx_rec - N["arxiv_unicos"]) + (s2_rec - 244), 244 - N["s2_nuevos"]
uniq, c12, c123 = N["unicos"], N["c12"], N["c123"]
assert arx_rec + s2_rec - dup_in - dup_between == uniq
F = lambda s: ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", s)
FONT, BOLD, SMALL = F(30), ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32, index=1), F(25)
INK, MUT, BOX, STRIP = (25, 25, 25), (95, 95, 95), (255, 255, 255), (222, 232, 244)
W, H = 1700, 1560
im = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(im)

def box(x, y, w, h, lines, bold_first=True, fill=BOX):
    d.rectangle([x, y, x + w, y + h], fill=fill, outline=INK, width=3)
    hs = [(BOLD if (i == 0 and bold_first) else FONT) for i in range(len(lines))]
    tot = sum(f.size + 10 for f in hs) - 10; cy = y + (h - tot) / 2
    for t, f in zip(lines, hs):
        tw = d.textlength(t, font=f); d.text((x + (w - tw) / 2, cy), t, fill=INK, font=f); cy += f.size + 10
def arrow(x1, y1, x2, y2):
    d.line([x1, y1, x2, y2], fill=INK, width=3)
    if x1 == x2: d.polygon([(x2, y2), (x2 - 11, y2 - 20), (x2 + 11, y2 - 20)], fill=INK)
    else: d.polygon([(x2, y2), (x2 - 20, y2 - 11), (x2 - 20, y2 + 11)], fill=INK)
def strip(y1, y2, label):
    d.rectangle([20, y1, 100, y2], fill=STRIP, outline=INK, width=2)
    t = Image.new("RGBA", (int(d.textlength(label, font=BOLD)) + 10, 44), (0, 0, 0, 0)); ImageDraw.Draw(t).text((5, 2), label, fill=INK, font=BOLD)
    t = t.rotate(90, expand=True); im.paste(t, (60 - t.width // 2, (y1 + y2) // 2 - t.height // 2), t)

MX, MW, RX, RW = 150, 700, 960, 690
# Identification
strip(40, 330, "Identification")
box(MX, 40, MW, 290, ["Records identified from databases", f"arXiv, 11 Oct 2026 (n = {arx_rec})", f"Semantic Scholar, 18 Oct 2026 (n = {s2_rec})", "5 search strings (S1 to S5)"])
box(RX, 60, RW, 250, ["Records removed before screening", f"Duplicates within a source (n = {dup_in})", f"Duplicates between sources (n = {dup_between})"])
arrow(MX + MW, 185, RX, 185)
arrow(MX + MW // 2, 330, MX + MW // 2, 440)
# Screening
strip(440, 900, "Screening")
box(MX, 440, MW, 150, ["Unique records screened", f"by title and abstract (n = {uniq})"])
box(RX, 440, RW, 150, ["Excluded: C1 and C2 not both met", f"(n = {uniq - c12})"])
arrow(MX + MW, 515, RX, 515)
arrow(MX + MW // 2, 590, MX + MW // 2, 710)
box(MX, 710, MW, 150, ["Records meeting C1 and C2", f"(n = {c12})"])
box(RX, 700, RW, 170, ["Excluded: neither few data nor an", "aerial, agricultural, or medical", f"domain, criterion C3 (n = {c12 - c123})"])
arrow(MX + MW, 785, RX, 785)
arrow(MX + MW // 2, 860, MX + MW // 2, 990)
# Included
strip(990, 1400, "Included")
box(MX, 990, MW, 200, ["Records meeting C1, C2, and C3", f"(n = {c123})", "Titles reviewed; abstracts of", "the closest ones read"])
arrow(MX + MW // 2, 1190, MX + MW // 2, 1260)
box(MX, 1260, MW, 140, ["Works that study the review", "question (n = 0)"], fill=(238, 246, 238))
box(RX, 1200, RW, 200, ["Closest works (both medical)", "Fallah and Herzog, 2026", "Dombrowski et al., 2026"], bold_first=True)
arrow(MX + MW, 1330, RX, 1330)
note = ["Screening by keyword rules on title and abstract, single reviewer. Records found in both", "sources kept their arXiv screening; Semantic Scholar-only records used equivalent rules.", "C1: varies the autoencoder or its data. C2: measures generation. C3: few data or aerial,", "agricultural, or medical domain."]
for i, t in enumerate(note): d.text((150, 1440 + i * 30), t, fill=MUT, font=SMALL)
im.save("Imagenes/prisma_flow.png", dpi=(200, 200)); im.save("docs/prisma_flow.png", dpi=(200, 200))
print("ok", dict(dup_in=dup_in, dup_between=dup_between, uniq=uniq, c12=c12, c123=c123))
