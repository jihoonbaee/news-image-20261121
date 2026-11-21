#!/usr/bin/env python3
"""news-image-20261121 -- render the entry image with Pillow (local build).

Draws a newspaper front page (1024x1024 PNG) summing up Saturday
21 November 2026 from stories verified by ~05:00 UTC. This script is a
LOCAL build tool: the submitted program is main.ts, which only copies
entry.png to /output. Pillow runs here on the build machine only.

The script FAILS LOUDLY if any headline or sub-text exceeds its line
budget (grid headline 2 lines, grid sub 2 lines, band headline 1 line):
no text is ever silently truncated.

Run:  python3 render.py            (writes ./entry.png)
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (26, 26, 26)
RED = (160, 30, 30)
GREY = (96, 96, 96)
LINE = (200, 192, 178)
MARGIN = 36

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def serif_b(s):
    return font("DejaVuSerif-Bold.ttf", s)


def sans_b(s):
    return font("DejaVuSans-Bold.ttf", s)


def sans(s):
    return font("DejaVuSans.ttf", s)


def serif(s):
    return font("DejaVuSerif.ttf", s)


def fold(text, fnt, max_w, draw):
    """Greedy word wrap; returns the lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_icon(draw, kind, box, color):
    """Small flat pictogram for a story. box = (x0, y0, x1, y1)."""
    x0, y0, x1, y1 = box
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    if kind == "missile":
        # Shield (left) + thick diagonal missile + intercept burst.
        draw.polygon([(x0 + 6, y0 + 6), (x0 + 44, y0 + 6),
                      (x0 + 44, y0 + 34), (x0 + 25, y0 + 56),
                      (x0 + 6, y0 + 34)], outline=color, width=4)
        # Missile body: thick bar from tail (lower left) to nose (upper
        # right), built from the direction vector and its perpendicular.
        tx, ty = x0 + 62, y1 - 14          # tail centre
        nx, ny = x1 - 22, y0 + 16          # nose base centre
        dx, dy = nx - tx, ny - ty
        ln = math.hypot(dx, dy)
        ux, uy = dx / ln, dy / ln          # unit along body
        px, py = -uy, ux                   # unit perpendicular
        hw = 7                             # half width of body
        draw.polygon([(tx + px * hw, ty + py * hw),
                      (nx + px * hw, ny + py * hw),
                      (nx + ux * 18, ny + uy * 18),
                      (nx - px * hw, ny - py * hw),
                      (tx - px * hw, ty - py * hw)], fill=color)
        # Fins at the tail.
        draw.polygon([(tx, ty), (tx - px * 14, ty - py * 14),
                      (tx + ux * 14, ty + uy * 14)], fill=color)
        draw.polygon([(tx, ty), (tx + px * 14, ty + py * 14),
                      (tx + ux * 14, ty + uy * 14)], fill=color)
        # Flame behind the tail.
        draw.polygon([(tx - ux * 4, ty - uy * 4),
                      (tx - ux * 20, ty - uy * 20),
                      (tx - ux * 4 - px * 5, ty - uy * 4 - py * 5)],
                     fill=(220, 120, 0))
        # Intercept burst where shield meets missile path.
        bx, by = x0 + 60, y0 + 24
        for ang in range(0, 360, 45):
            a = math.radians(ang)
            draw.line([bx, by, bx + int(13 * math.cos(a)),
                       by + int(13 * math.sin(a))], fill=RED, width=3)
    elif kind == "seismo":
        # Seismograph zigzag on a strip, cracked ground below.
        draw.rectangle([x0 + 4, y0 + 6, x1 - 4, y0 + 40], outline=color,
                       width=3)
        pts = [(x0 + 10, y0 + 23), (x0 + 26, y0 + 23), (x0 + 34, y0 + 12),
               (x0 + 42, y0 + 34), (x0 + 50, y0 + 14), (x0 + 58, y0 + 30),
               (x0 + 66, y0 + 23), (x1 - 10, y0 + 23)]
        draw.line(pts, fill=RED, width=3, joint="curve")
        draw.line([x0 + 10, y1 - 8, cx - 8, y1 - 18, cx + 2, y1 - 12,
                   cx + 18, y1 - 20, x1 - 10, y1 - 10], fill=color, width=3)
    elif kind == "cop":
        # Globe with meridians + leaf.
        draw.ellipse([x0 + 8, y0 + 2, x0 + 58, y0 + 52], outline=color,
                     width=4)
        draw.arc([x0 + 20, y0 + 2, x0 + 46, y0 + 52], start=90, end=270,
                 fill=color, width=3)
        draw.line([x0 + 8, y0 + 27, x0 + 58, y0 + 27], fill=color, width=3)
        draw.arc([x0 + 58, y0 + 22, x1 - 2, y0 + 54], start=180, end=360,
                 fill=(30, 120, 70), width=4)
        draw.line([x0 + 74, y0 + 44, x0 + 88, y0 + 30], fill=(30, 120, 70),
                  width=3)
    elif kind == "cricket":
        # Bat (tilted) + red ball with seam.
        draw.polygon([(x0 + 18, y0 + 6), (x0 + 34, y0 + 2),
                      (x0 + 58, y0 + 44), (x0 + 46, y0 + 54)],
                     fill=(210, 180, 120), outline=(140, 100, 50))
        draw.line([x0 + 46, y0 + 54, x0 + 60, y0 + 62], fill=(140, 100, 50),
                  width=5)
        draw.ellipse([x1 - 34, y1 - 32, x1 - 8, y1 - 6], fill=(170, 30, 30))
        draw.arc([x1 - 30, y1 - 28, x1 - 12, y1 - 10], start=300, end=60,
                 fill=(255, 255, 255), width=2)
    elif kind == "falling":
        # Descending bars + red down arrow.
        bh = y1 - y0
        base = y1 - 4
        heights = [int(bh * f) for f in (0.72, 0.56, 0.40, 0.26)]
        bw = 20
        for i, hh in enumerate(heights):
            bx = x0 + 8 + i * (bw + 6)
            draw.rectangle([bx, base - hh, bx + bw, base], fill=color)
        draw.line([x0 + 8, y0 + 8, x1 - 10, y0 + 34], fill=RED, width=4)
        draw.polygon([(x1 - 10, y0 + 34), (x1 - 30, y0 + 28),
                      (x1 - 16, y0 + 44)], fill=RED)
    elif kind == "shield":
        # NATO-style shield + four-point compass star, scaled to the box
        # (the band strip is short, so the shield must fit its height).
        bh = y1 - y0 - 4
        bw = min((x1 - x0) * 0.5, bh * 0.85)
        sx0, sx1 = cx - bw, cx + bw
        sy0, sy1 = y0 + 2, y0 + 2 + bh
        draw.polygon([(sx0, sy0), (sx1, sy0), (sx1, sy0 + bh * 0.55),
                      (cx, sy1), (sx0, sy0 + bh * 0.55)], fill=color)
        scx, scy = cx, sy0 + bh * 0.42
        r = bw * 0.55
        draw.polygon([(scx, scy - r), (scx + r * 0.3, scy - r * 0.3),
                      (scx + r, scy), (scx + r * 0.3, scy + r * 0.3),
                      (scx, scy + r), (scx - r * 0.3, scy + r * 0.3),
                      (scx - r, scy), (scx - r * 0.3, scy - r * 0.3)],
                     fill=(255, 255, 255))


STORIES = [
    dict(kicker="MIDDLE EAST  |  CONFLICT", icon="missile",
         color=(166, 30, 30),
         headline="MISSILES OVER RIYADH INTERCEPTED",
         sub="Saudi-led coalition says it destroyed three Houthi ballistic "
             "missiles fired at Riyadh, the second attack in days."),
    dict(kicker="SOUTH AMERICA  |  DISASTER", icon="seismo",
         color=(140, 90, 30),
         headline="M6.8 QUAKE SHAKES PERU",
         sub="USGS puts the tremor near Jun\u00edn at 6.8; felt in Lima, "
             "no major damage reported yet."),
    dict(kicker="CLIMATE  |  COP31", icon="cop", color=(30, 120, 70),
         headline="COP31 TALKS RUN PAST DEADLINE",
         sub="No deal yet as talks run past deadline; an earlier draft "
             "dropped all fossil-fuel mentions."),
    dict(kicker="SPORT  |  CRICKET", icon="cricket", color=(110, 60, 160),
         headline="RAHUL COMPLETES SENA CENTURY SET",
         sub="100 off 207 balls in Wellington \u2014 first Indian opener "
             "with Test tons in all four SENA nations."),
    dict(kicker="MARKETS  |  UNITED STATES", icon="falling",
         color=(40, 80, 140),
         headline="WALL ST IN CORRECTION",
         sub="Friday\u2019s close, reported in Asia: S&P \u22123.7%, "
             "Nasdaq \u22125.3%; Nasdaq erases its 2026 gains."),
    dict(kicker="EUROPE  |  SECURITY", icon="shield", color=(0, 110, 130),
         headline="NATO CHIEF HEADS TO WARSAW",
         sub="Rutte visits Poland after Russian missiles landed there; "
             "Warsaw calls it a deliberate provocation."),
]

ALSO_TODAY = ("ALSO TODAY:  Florida floods spread north  \u2022  "
              "Las Vegas GP qualifying  \u2022  "
              "US Senate honours Fiona the hippo")

DATE_LINE = "SATURDAY  \u2022  21 NOVEMBER 2026"
SUB_LINE = "Six stories that defined the day \u2014 as reported by 05:00 UTC"
NOTE = ("Draft edition \u2014 covers the day so far; "
        "refresh after 21 November ends.")

PROBLEMS = []


def story_panel(draw, st, x, y, w, h, lead=False, band=False):
    draw.rectangle([x, y, x + w, y + h], outline=LINE, width=2)
    draw.rectangle([x, y, x + w, y + 5], fill=st["color"])
    pad = 16
    tx = x + pad
    ty = y + 14
    kicker_f = sans_b(19 if lead else 17)
    draw.text((tx, ty), st["kicker"], font=kicker_f, fill=st["color"])
    ty += 30 if lead else 26
    head_size = 40 if lead else (28 if band else 26)
    head_f = sans_b(head_size)
    head_lh = 46 if lead else (34 if band else 31)
    icon_w, icon_h = (190, 92) if lead else ((118, 34) if band else (118, 62))
    icon_box = (x + w - icon_w - pad, ty, x + w - pad, ty + icon_h)
    draw_icon(draw, st["icon"], icon_box, st["color"])
    text_w = w - 2 * pad - (icon_w + 14)
    max_head_lines = 1 if band else 2
    head_lines = fold(st["headline"], head_f, text_w, draw)
    if len(head_lines) > max_head_lines:
        PROBLEMS.append("HEADLINE %d lines (max %d): %r"
                        % (len(head_lines), max_head_lines, st["headline"]))
    for line in head_lines[:max_head_lines]:
        draw.text((tx, ty), line, font=head_f, fill=INK)
        ty += head_lh
    ty += 6
    sub_size = 21 if lead else 18
    sub_f = sans(sub_size)
    sub_lh = 26 if lead else 23
    sub_w = w - 2 * pad
    sub_lines = fold(st["sub"], sub_f, sub_w, draw)
    if len(sub_lines) > 2:
        PROBLEMS.append("SUB %d lines (max 2): %r"
                        % (len(sub_lines), st["sub"]))
    for line in sub_lines[:2]:
        draw.text((tx, ty), line, font=sub_f, fill=(60, 60, 60))
        ty += sub_lh
    return ty


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    d.rectangle([0, 0, W, 6], fill=RED)
    y = 22
    title = "THE WORLD IN ONE DAY"
    tf = serif_b(56)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, y), title, font=tf, fill=INK)
    y += 66
    df = sans_b(34)
    dw = d.textlength(DATE_LINE, font=df)
    d.text(((W - dw) / 2, y), DATE_LINE, font=df, fill=RED)
    y += 46
    sf = serif(21)
    sw = d.textlength(SUB_LINE, font=sf)
    d.text(((W - sw) / 2, y), SUB_LINE, font=sf, fill=GREY)
    y += 36
    d.line([MARGIN, y, W - MARGIN, y], fill=INK, width=3)
    y += 12

    # --- lead story, full width ---
    lead_h = 216
    story_panel(d, STORIES[0], MARGIN, y, W - 2 * MARGIN, lead_h, lead=True)
    y += lead_h + 12

    # --- grid 2x2 ---
    gap = 12
    col_w = (W - 2 * MARGIN - gap) // 2
    row_h = 182
    for i, st in enumerate(STORIES[1:5]):
        gx = MARGIN + (i % 2) * (col_w + gap)
        gy = y + (i // 2) * (row_h + gap)
        story_panel(d, st, gx, gy, col_w, row_h)
    y += 2 * row_h + gap + 12

    # --- bottom band: sixth story ---
    story_panel(d, STORIES[5], MARGIN, y, W - 2 * MARGIN, 128, band=True)
    y += 128 + 12

    # --- footer ---
    d.line([MARGIN, y, W - MARGIN, y], fill=RED, width=2)
    y += 10
    ff = sans(18)
    also_lines = fold(ALSO_TODAY, ff, W - 2 * MARGIN, d)
    if len(also_lines) > 2:
        PROBLEMS.append("ALSO %d lines (max 2)" % len(also_lines))
    for line in also_lines[:2]:
        d.text((MARGIN, y), line, font=ff, fill=INK)
        y += 23
    y += 2
    d.text((MARGIN, y), NOTE, font=serif(17), fill=GREY)

    if PROBLEMS:
        print("LAYOUT PROBLEMS:")
        for p in PROBLEMS:
            print(" -", p)
        raise SystemExit(1)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size,
          os.path.getsize("entry.png"), "bytes")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
