# osso-lmarbles: the Nokia N900's Marbles for Maemo Leste and FreeBSD

Marbles, the Atomix-like puzzle game of Maemo 5 (Fremantle): Michael
Speck's [LMarbles](https://lgames.sourceforge.net/) as Nokia adapted it
(GPL), started from `osso-games-startup` through `hildon-games-wrapper`.
Imported from the Fremantle source by android-808; ported here to today's
Maemo Leste and to Hildon on FreeBSD (see `debian/changelog`).

- **Pictures**: the N900's were Nokia's (`osso-graphics-game-lmarbles`,
  not free). The marbles, walls, floors, arrows, teleports and
  backgrounds are LMarbles' own (1.0.8, GPL); the side panel, undo
  button, dialog and start picture are drawn by `data/make-art.py`.
- **Settings from the session's GConf** (libhgw looked on the system bus).
- **Full screen at any size** with sdl12-compat: the 800x480 game is
  scaled to the screen, keeping its shape.

## Build

Debian/Leste: `dpkg-buildpackage -b -us -uc` (needs
`hildon-games-wrapper-dev`, `osso-games-startup-dev`, SDL 1.2 or
sdl12-compat with SDL_mixer and SDL_image). FreeBSD: part of
[pro1x-maemo-leste](https://github.com/smatkovi/pro1x-maemo-leste)'s
`freebsd/hildon` build.

To remake the pictures: `python3 data/make-art.py <lmarbles-1.0.8>/src/gfx`
(Pillow; LMarbles 1.0.8 is Debian's `lmarbles_1.0.8.orig.tar.gz`).

## Licence

GPL 2 or later.
