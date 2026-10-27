dbusdir=$(prefix)/share/dbus-1/services
dbus_DATA=com.nokia.osso_lmarbles.service \
	  com.nokia.osso_lmarbles.startup.service

desktopdir=$(datadir)/applications/hildon
desktop_DATA = osso_lmarbles.desktop

configdir = $(datadir)/osso-lmarbles
config_DATA = osso_lmarbles.conf

dbuswrapperdir=$(datadir)/osso-lmarbles
dbuswrapper_DATA = osso_lmarbles.game

lmarbleslevelsdir =$(datadir)/osso-lmarbles/levels
lmarbleslevels_DATA = levels/Original 

lmarblesprofiledir=$(datadir)/osso-lmarbles/profile
lmarblesprofile_DATA = profile/lmarbles_profile

# The pictures (make-art.py: LMarbles' own, the rest drawn there), below
# $(datadir)/osso-lmarbles/gfx as configure's lmarblesgfxdir
lmarblesgfxbasedir = $(datadir)/osso-lmarbles
nobase_lmarblesgfxbase_DATA = \
	gfx/board.png \
	gfx/dialog/dialog_background_tile.bmp \
	gfx/dialog/dialog_bottom_left.bmp \
	gfx/dialog/dialog_bottom_right.bmp \
	gfx/dialog/dialog_bottom_tile.bmp \
	gfx/dialog/dialog_left_tile.bmp \
	gfx/dialog/dialog_right_tile.bmp \
	gfx/dialog/dialog_top_left.bmp \
	gfx/dialog/dialog_top_right.bmp \
	gfx/dialog/dialog_top_tile.bmp \
	gfx/dialog/No-button.bmp \
	gfx/dialog/Yes-button.bmp \
	gfx/figure.bmp \
	gfx/lights.bmp \
	gfx/marbles.png \
	gfx/metal/arrow_d.bmp \
	gfx/metal/arrow_l.bmp \
	gfx/metal/arrow_r.bmp \
	gfx/metal/arrow_u.bmp \
	gfx/metal/background.jpg \
	gfx/metal/barrier_lr.bmp \
	gfx/metal/barrier_ud.bmp \
	gfx/metal/floor.bmp \
	gfx/metal/teleport0.bmp \
	gfx/metal/teleport1.bmp \
	gfx/metal/teleport2.bmp \
	gfx/metal/teleport3.bmp \
	gfx/metal/wall.bmp \
	gfx/metal/wall_crumble.bmp \
	gfx/m_frame.bmp \
	gfx/m_sframe.bmp \
	gfx/stone/arrow_d.bmp \
	gfx/stone/arrow_l.bmp \
	gfx/stone/arrow_r.bmp \
	gfx/stone/arrow_u.bmp \
	gfx/stone/background.jpg \
	gfx/stone/barrier_lr.bmp \
	gfx/stone/barrier_ud.bmp \
	gfx/stone/floor.bmp \
	gfx/stone/teleport0.bmp \
	gfx/stone/teleport1.bmp \
	gfx/stone/teleport2.bmp \
	gfx/stone/teleport3.bmp \
	gfx/stone/wall.bmp \
	gfx/stone/wall_crumble.bmp \
	gfx/undo-button.bmp \
	gfx/undo-button_dimmed.bmp \
	gfx/undo-button_pressed.bmp \
	gfx/wood/arrow_d.bmp \
	gfx/wood/arrow_l.bmp \
	gfx/wood/arrow_r.bmp \
	gfx/wood/arrow_u.bmp \
	gfx/wood/background.jpg \
	gfx/wood/barrier_lr.bmp \
	gfx/wood/barrier_ud.bmp \
	gfx/wood/floor.bmp \
	gfx/wood/teleport0.bmp \
	gfx/wood/teleport1.bmp \
	gfx/wood/teleport2.bmp \
	gfx/wood/teleport3.bmp \
	gfx/wood/wall.bmp \
	gfx/wood/wall_crumble.bmp

startupdir = $(datadir)/pixmaps
startup_DATA = osso-games-startup-lmarbles.png

lmarblessoundsdir =$(datadir)/osso-lmarbles/sounds
lmarblessounds_DATA = sounds/alarm.wav \
sounds/arrow.wav \
sounds/click.wav \
sounds/explode.wav \
sounds/score.wav \
sounds/select.wav \
sounds/stop.wav \
sounds/teleport.wav

edit = sed \
       -e 's,@datadir\@,$(datadir),g' \
       -e 's,@prefix\@,$(prefix),g'   \
       -e 's,@VERSION\@,$(VERSION),g'
	   
osso_lmarbles.conf: osso_lmarbles.conf.in
	        @$(edit) $< > $@

osso_lmarbles.sh: osso_lmarbles.sh.in
	        @$(edit) $< > $@
			
backupconfigurationdir=$(sysconfdir)/osso-backup/applications
backupconfiguration_DATA=osso-lmarbles.conf

EXTRA_DIST = $(dbus_DATA) $(desktop_DATA) $(dbuswrapper_DATA) $(lmarbleslevels_DATA) $(lmarblessounds_DATA) \
	     $(nobase_lmarblesgfxbase_DATA) $(startup_DATA) make-art.py \
	     $(lmarblesprofile_DATA) $(config_DATA) $(backupconfiguration_DATA)
