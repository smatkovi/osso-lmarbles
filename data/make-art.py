#!/usr/bin/env python3
"""Makes the pictures of osso-lmarbles in data/gfx/. On the N900 they were
Nokia's (osso-graphics-game-lmarbles) and are not part of this source.

The marbles, frames, walls, floors, arrows, barriers, teleports and
backgrounds are LMarbles' own, by Michael Speck (GPL 2 or later), from
LMarbles 1.0.8 (lmarbles_1.0.8.orig.tar.gz, Debian's source): its
src/gfx directory is the argument. The side panel, the undo button, the
dialog and the start screen's picture are drawn here, in the style of
osso-chess-ui's.

    python3 data/make-art.py .../lmarbles-1.0.8/src/gfx
                                  (needs Pillow)
"""
import os
import shutil
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "gfx")

FRAME = (46, 52, 58)
PANEL = (58, 65, 72)
WELL = (20, 22, 26)
TEXT = (225, 228, 230)
ACCENT = (255, 196, 0)
YES, NO = (88, 170, 92), (196, 74, 70)


def font(size):
    for f in ("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/local/share/fonts/dejavu/DejaVuSans-Bold.ttf"):
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def save_bmp(im, name):
    im.convert("RGB").save(os.path.join(OUT, name), "BMP")


def from_lmarbles(src):
    """LMarbles' own pictures, at the names and sizes osso-lmarbles loads"""
    marbles = Image.open(os.path.join(src, "marbles.bmp")).convert("RGB")
    marbles.save(os.path.join(OUT, "marbles.png"))
    for f in ("m_frame.bmp", "m_sframe.bmp"):
        shutil.copy(os.path.join(src, f), os.path.join(OUT, f))
    # the level's figure: a marble of each colour, 16x16 (10 colours)
    fig = Image.new("RGB", (16, 160), (0, 0, 0))
    for c in range(10):
        m = marbles.crop((0, c * 32, 32, c * 32 + 32)).resize((16, 16), Image.LANCZOS)
        fig.paste(m, (0, c * 16))
    save_bmp(fig, "figure.bmp")
    # the lights, 4x 32x32 (LMarbles' 12x12)
    save_bmp(Image.open(os.path.join(src, "lights.bmp")).convert("RGB")
             .resize((128, 32), Image.LANCZOS), "lights.bmp")
    for st in ("wood", "stone", "metal"):
        os.makedirs(os.path.join(OUT, st), exist_ok=True)
        for f in os.listdir(os.path.join(src, st)):
            p = os.path.join(src, st, f)
            if f == "background.bmp":
                Image.open(p).convert("RGB").save(
                    os.path.join(OUT, st, "background.jpg"), quality=90)
            else:
                shutil.copy(p, os.path.join(OUT, st, f))


def rounded(d, box, fill, outline=None, radius=10, width=2):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def board():
    """The panel right of the level, 360x480: the level's name at
    (102, 10) 258x70, undo at (56, 110) 66x66, the time at (172, 104),
    the level's figure at (171, 162) 156x116, the marbles' state at
    (72, 318) 264x120 (src/game.c); the back button at the top right."""
    im = Image.new("RGB", (360, 480), FRAME)
    d = ImageDraw.Draw(im)
    rounded(d, (96, 6, 354, 84), WELL, PANEL)
    rounded(d, (50, 104, 128, 182), PANEL)
    rounded(d, (166, 98, 354, 142), WELL, PANEL)
    rounded(d, (166, 154, 354, 300), WELL, PANEL)
    rounded(d, (64, 310, 354, 474), WELL, PANEL)
    rounded(d, (8, 6, 40, 474), PANEL)
    return im


def undo(state):
    im = Image.new("RGB", (66, 66), PANEL)
    d = ImageDraw.Draw(im)
    face = {"normal": (82, 92, 102), "pressed": ACCENT, "dimmed": (66, 72, 78)}[state]
    arrow = {"normal": TEXT, "pressed": WELL, "dimmed": (120, 126, 132)}[state]
    rounded(d, (3, 3, 62, 62), face, radius=12)
    d.polygon([(20, 33), (40, 17), (40, 49)], fill=arrow)
    return im


def dialog():
    """The question dialog's frame tiles and its yes and no buttons"""
    os.makedirs(os.path.join(OUT, "dialog"), exist_ok=True)
    big = Image.new("RGB", (96, 96), FRAME)
    d = ImageDraw.Draw(big)
    rounded(d, (0, 0, 95, 95), PANEL, ACCENT, radius=14, width=3)
    tiles = {
        "dialog_top_left.bmp": (0, 0, 16, 16), "dialog_top_right.bmp": (80, 0, 96, 16),
        "dialog_bottom_left.bmp": (0, 80, 16, 96), "dialog_bottom_right.bmp": (80, 80, 96, 96),
        "dialog_top_tile.bmp": (16, 0, 80, 16), "dialog_bottom_tile.bmp": (16, 80, 80, 96),
        "dialog_left_tile.bmp": (0, 16, 16, 80), "dialog_right_tile.bmp": (80, 16, 96, 80),
        "dialog_background_tile.bmp": (40, 40, 56, 56),
    }
    for name, box in tiles.items():
        save_bmp(big.crop(box), os.path.join("dialog", name))
    for name, colour, left, mark in (("Yes-button.bmp", YES, True, "✓"),
                                     ("No-button.bmp", NO, False, "✕")):
        im = Image.new("RGB", (194, 82), PANEL)
        d = ImageDraw.Draw(im)
        rounded(d, (4, 8, 189, 73), (82, 92, 102), radius=30)
        cx = 44 if left else 150
        d.ellipse((cx - 28, 13, cx + 28, 69), fill=colour, outline=TEXT, width=3)
        f = font(36)
        l, t, r, b = d.textbbox((0, 0), mark, font=f)
        d.text((cx - (r - l) / 2 - l, 41 - (b - t) / 2 - t), mark, font=f, fill=TEXT)
        save_bmp(im, os.path.join("dialog", name))


def startup(src):
    """osso-games-startup's picture of the game, 648x180"""
    im = Image.new("RGBA", (648, 180), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    rounded(d, (0, 0, 647, 179), FRAME + (255,), radius=16)
    marbles = Image.open(os.path.join(src, "marbles.bmp")).convert("RGB")
    for i, c in enumerate((1, 2, 3, 5, 6)):
        m = marbles.crop((0, c * 32, 32, c * 32 + 32)).resize((64, 64), Image.LANCZOS)
        mask = m.convert("L").point(lambda v: 255 if v > 12 else 0)
        im.paste(m, (28 + i * 56, 58 + (i % 2) * 24), mask)
    f = font(64)
    l, t, r, b = d.textbbox((0, 0), "Marbles", font=f)
    d.text((340 + (290 - (r - l)) / 2 - l, 90 - (b - t) / 2 - t), "Marbles", font=f, fill=TEXT)
    im.save(os.path.join(HERE, "osso-games-startup-lmarbles.png"))


def main():
    src = sys.argv[1]
    os.makedirs(OUT, exist_ok=True)
    from_lmarbles(src)
    board().save(os.path.join(OUT, "board.png"))
    for state, name in (("normal", "undo-button.bmp"), ("pressed", "undo-button_pressed.bmp"),
                        ("dimmed", "undo-button_dimmed.bmp")):
        save_bmp(undo(state), name)
    dialog()
    startup(src)


if __name__ == "__main__":
    sys.exit(main())
