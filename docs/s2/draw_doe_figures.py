"""Figures of section 2.2.10 (design of experiments and statistical analysis). All values are illustrative.
A) main effect and interaction, B) the half fraction 2^(3-1) and the alias C = AB, C) the three outcomes of an effect
against the equivalence margin. Run from the repository root: python3 docs/s2/draw_doe_figures.py
Outputs: Imagenes/doe_effects.png, Imagenes/doe_fraction.png, Imagenes/doe_equivalence.png
Drawn with PIL at 3x and reduced, like the other figures of the proposal."""
import math
from PIL import Image, ImageDraw, ImageFont

S = 3                                           # supersampling factor
HEL = "/System/Library/Fonts/Helvetica.ttc"
INK, MUT, GRID = (40, 40, 40), (105, 105, 105), (222, 222, 222)
BLUE, ORANGE, NEUTRAL = (31, 95, 168), (217, 115, 26), (70, 70, 70)
BAND, SAND = (236, 236, 236), (250, 232, 210)


class Canvas:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.im = Image.new("RGB", (w * S, h * S), (255, 255, 255))
        self.d = ImageDraw.Draw(self.im)

    def font(self, size, bold=False):
        return ImageFont.truetype(HEL, int(size * S), index=1 if bold else 0)

    def line(self, p, q, color=INK, width=3, dash=None):
        (x1, y1), (x2, y2) = p, q
        if not dash:
            self.d.line([x1 * S, y1 * S, x2 * S, y2 * S], fill=color, width=int(width * S))
            return
        L = math.hypot(x2 - x1, y2 - y1)
        n = int(L // (dash[0] + dash[1])) + 1
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        for i in range(n):
            a, b = i * (dash[0] + dash[1]), min(i * (dash[0] + dash[1]) + dash[0], L)
            self.d.line([(x1 + ux * a) * S, (y1 + uy * a) * S, (x1 + ux * b) * S, (y1 + uy * b) * S],
                        fill=color, width=int(width * S))

    def rect(self, box, fill=None, outline=None, width=2):
        x1, y1, x2, y2 = box
        self.d.rectangle([x1 * S, y1 * S, x2 * S, y2 * S], fill=fill, outline=outline, width=int(width * S))

    def circle(self, c, r, fill=None, outline=None, width=3):
        x, y = c
        self.d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=fill, outline=outline, width=int(width * S))

    def square(self, c, r, fill=None, outline=None, width=3):
        x, y = c
        self.d.rectangle([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=fill, outline=outline, width=int(width * S))

    def diamond(self, c, r, fill=None, outline=None):
        x, y = c
        self.d.polygon([((x) * S, (y - r) * S), ((x + r) * S, y * S), (x * S, (y + r) * S), ((x - r) * S, y * S)],
                       fill=fill, outline=outline)

    def text(self, xy, s, size=36, color=INK, bold=False, anchor="la"):
        self.d.text((xy[0] * S, xy[1] * S), s, fill=color, font=self.font(size, bold), anchor=anchor)

    def vtext(self, xy, s, size=36, color=INK):
        """Text rotated 90 degrees counterclockwise, centered at xy."""
        f = self.font(size)
        w = int(self.d.textlength(s, font=f)) + 8
        tmp = Image.new("RGBA", (w, int(size * S * 1.6)), (255, 255, 255, 0))
        ImageDraw.Draw(tmp).text((4, 4), s, fill=color, font=f)
        tmp = tmp.rotate(90, expand=True)
        self.im.paste(tmp, (int(xy[0] * S - tmp.width / 2), int(xy[1] * S - tmp.height / 2)), tmp)

    def arrow(self, p, q, color=INK, width=4, head=16):
        self.line(p, q, color, width)
        ang = math.atan2(q[1] - p[1], q[0] - p[0])
        a1, a2 = ang + math.radians(150), ang - math.radians(150)
        self.d.polygon([q[0] * S, q[1] * S, (q[0] + head * math.cos(a1)) * S, (q[1] + head * math.sin(a1)) * S,
                        (q[0] + head * math.cos(a2)) * S, (q[1] + head * math.sin(a2)) * S], fill=color)

    def save(self, path):
        out = self.im.resize((self.w, self.h), Image.LANCZOS)
        out.save(path, dpi=(200, 200))
        print("ok", path, out.size)


# --------------------------------------------------------------------------------------------------- A
def fig_effects():
    c = Canvas(1700, 700)
    ylo, yhi, top, bot = 148, 164, 130, 500          # FID range and pixel rows of the plot area
    py = lambda v: bot - (v - ylo) / (yhi - ylo) * (bot - top)
    panels = [
        (170, "(a) No interaction", [160, 154], [156, 150],
         ["Effect of A: −6 with B off and −6 with B on.", "Main effect of A = −6."]),
        (960, "(b) Interaction", [160, 154], [156, 162],
         ["Effect of A: −6 with B off and +6 with B on.", "Main effect of A = 0, yet A matters."]),
    ]
    c.vtext((45, (top + bot) / 2), "FID (illustrative)", 36, MUT)
    for x0, title, off, on, notes in panels:
        c.text((x0 - 100, 28), title, 44, INK, bold=True)
        for v in (150, 155, 160):
            c.line((x0, py(v)), (x0 + 620, py(v)), GRID, 2)
            c.text((x0 - 14, py(v)), str(v), 34, MUT, anchor="rm")
        c.line((x0, bot), (x0 + 620, bot), INK, 3)
        xs = (x0 + 90, x0 + 420)
        c.text((xs[0], bot + 22), "A off", 36, INK, anchor="ma")
        c.text((xs[1], bot + 22), "A on", 36, INK, anchor="ma")
        # B off: solid blue with circles; B on: dashed orange with squares
        c.line((xs[0], py(off[0])), (xs[1], py(off[1])), BLUE, 6)
        c.line((xs[0], py(on[0])), (xs[1], py(on[1])), ORANGE, 6, dash=(26, 14))
        for x, v in zip(xs, off):
            c.circle((x, py(v)), 14, fill=BLUE)
        for x, v in zip(xs, on):
            c.square((x, py(v)), 13, fill=ORANGE)
        c.text((xs[1] + 34, py(off[1])), "B off", 34, INK, anchor="lm")
        c.text((xs[1] + 34, py(on[1])), "B on", 34, INK, anchor="lm")
        c.text((x0 - 100, bot + 85), notes[0], 34, INK)
        c.text((x0 - 100, bot + 130), notes[1], 34, INK, bold=True)
    c.save("Imagenes/doe_effects.png")


# --------------------------------------------------------------------------------------------------- B
def fig_fraction():
    c = Canvas(1700, 800)
    x0, y0, s, dx, dy = 150, 620, 300, 200, -160     # front-face lower-left corner, edge, depth offset
    pos = lambda a, b, cc: (x0 + (a + 1) / 2 * s + (b + 1) / 2 * dx, y0 - (cc + 1) / 2 * s + (b + 1) / 2 * dy)
    corners = [(a, b, cc) for a in (-1, 1) for b in (-1, 1) for cc in (-1, 1)]
    edges = [(p, q) for p in corners for q in corners if p < q and sum(u != v for u, v in zip(p, q)) == 1]
    chosen = [(-1, -1, 1), (-1, 1, -1), (1, -1, -1), (1, 1, 1)]          # C = A*B
    t1 = "Half fraction 2"; w1 = c.d.textlength(t1, font=c.font(44, True)) / S
    w2 = c.d.textlength("(3−1)", font=c.font(30, True)) / S
    c.text((60, 25), t1, 44, INK, bold=True)
    c.text((60 + w1 + 2, 16), "(3−1)", 30, INK, bold=True)
    c.text((60 + w1 + w2 + 14, 25), "with C = AB", 44, INK, bold=True)
    for p, q in edges:                                                    # back edges lighter
        back = p[1] == 1 and q[1] == 1
        c.line(pos(*p), pos(*q), (190, 190, 190) if back else (150, 150, 150), 3)
    for i, p in enumerate(chosen):                                        # the six diagonals of the tetrahedron
        for q in chosen[i + 1:]:
            c.line(pos(*p), pos(*q), BLUE, 3, dash=(16, 10))
    for p in corners:
        if p not in chosen:
            c.circle(pos(*p), 11, fill=(255, 255, 255), outline=(150, 150, 150), width=3)
    for n, p in enumerate(chosen, 1):
        x, y = pos(*p)
        c.circle((x, y), 22, fill=BLUE)
        c.text((x, y), str(n), 30, (255, 255, 255), bold=True, anchor="mm")
    # axes
    c.arrow((x0, y0 + 70), (x0 + s + 40, y0 + 70)); c.text((x0 + s + 62, y0 + 70), "A", 40, INK, bold=True, anchor="lm")
    c.arrow((x0 - 70, y0), (x0 - 70, y0 - s - 40)); c.text((x0 - 70, y0 - s - 62), "C", 40, INK, bold=True, anchor="mm")
    c.arrow((x0 + s + 55, y0 + 12), (x0 + s + 55 + dx * 0.55, y0 + 12 + dy * 0.55)); c.text((x0 + s + 55 + dx * 0.55 + 22, y0 + 12 + dy * 0.55 - 8), "B", 40, INK, bold=True, anchor="lm")
    c.text((x0 - 40, y0 + 120), "Filled corners: the 4 cells that are run.", 34, MUT)
    # table
    tx, ty, cw, rh = 930, 150, 130, 82
    heads = ["Cell", "A", "B", "C", "A×B"]
    rows = [(1, "−", "−", "+", "+"), (2, "−", "+", "−", "−"), (3, "+", "−", "−", "−"), (4, "+", "+", "+", "+")]
    c.rect((tx + 3 * cw, ty, tx + 5 * cw, ty + rh * 5), fill=SAND)
    for j, h in enumerate(heads):
        c.text((tx + j * cw + cw / 2, ty + rh / 2), h, 40, INK, bold=True, anchor="mm")
    c.line((tx, ty + rh), (tx + 5 * cw, ty + rh), INK, 3)
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            c.text((tx + j * cw + cw / 2, ty + rh * (i + 1.5)), str(v), 42, INK, anchor="mm")
    c.line((tx, ty + rh * 5), (tx + 5 * cw, ty + rh * 5), INK, 3)
    c.text((tx, ty + rh * 5 + 40), "The columns C and A×B are identical:", 36, INK)
    c.text((tx, ty + rh * 5 + 86), "their effects are aliased.", 36, INK, bold=True)
    c.text((tx, ty + rh * 5 + 150), "Defining relation I = ABC.", 34, MUT)
    c.save("Imagenes/doe_fraction.png")


# --------------------------------------------------------------------------------------------------- C
def fig_equivalence():
    c = Canvas(1700, 850)
    lo, hi, x_l, x_r = -15, 15, 130, 1620
    px = lambda v: x_l + (v - lo) / (hi - lo) * (x_r - x_l)
    delta, strip_h = 5, 100
    c.text((px(0), 28), "Margin ±Δ: effects inside it are treated as equivalent to zero", 38, INK, bold=True, anchor="ma")
    rows = [
        (100, BLUE, "circle", 8, (4, 12), "Supported", "the interval excludes zero"),
        (290, NEUTRAL, "diamond", 0.5, (-2.5, 3.5), "Refuted", "the interval lies inside ±Δ"),
        (480, ORANGE, "square", 3, (-6.5, 12.5), "Inconclusive", "the interval includes zero and goes beyond ±Δ"),
    ]
    for ly, col, shape, est, (a, b), name, why in rows:
        c.text((x_l, ly), name, 40, INK, bold=True)
        c.text((x_l + 25 + c.d.textlength(name, font=c.font(40, True)) / S, ly + 2), "— " + why, 36, INK)
        top, bot_s = ly + 62, ly + 62 + strip_h
        y = (top + bot_s) / 2
        c.rect((px(-delta), top, px(delta), bot_s), fill=BAND)
        c.line((px(-delta), top), (px(-delta), bot_s), MUT, 2, dash=(12, 8))
        c.line((px(delta), top), (px(delta), bot_s), MUT, 2, dash=(12, 8))
        c.line((px(0), top), (px(0), bot_s), INK, 3)
        c.line((px(a), y), (px(b), y), col, 7)
        c.line((px(a), y - 18), (px(a), y + 18), col, 7)
        c.line((px(b), y - 18), (px(b), y + 18), col, 7)
        if shape == "circle":
            c.circle((px(est), y), 17, fill=col)
        elif shape == "square":
            c.square((px(est), y), 16, fill=col)
        else:
            c.diamond((px(est), y), 22, fill=col)
    last = 480 + 62 + strip_h
    c.text((px(-delta), last + 10), "−Δ", 36, MUT, anchor="ma")
    c.text((px(delta), last + 10), "+Δ", 36, MUT, anchor="ma")
    ay = last + 72
    c.line((x_l, ay), (x_r, ay), INK, 3)
    for v in range(lo, hi + 1, 5):
        c.line((px(v), ay), (px(v), ay + 14), INK, 3)
        lab = "0" if v == 0 else (f"+{v}" if v > 0 else f"−{abs(v)}")
        c.text((px(v), ay + 22), lab, 34, INK, anchor="ma")
    c.text(((x_l + x_r) / 2, ay + 82), "Effect of a factor on the FID, in points (illustrative); bars are 95% confidence intervals", 34, MUT, anchor="ma")
    c.save("Imagenes/doe_equivalence.png")


if __name__ == "__main__":
    fig_effects()
    fig_fraction()
    fig_equivalence()
