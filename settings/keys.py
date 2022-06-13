# Antonio Sarosi
# TeteBD
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles
# https://github.com/TeteBD

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy
import os


mod = "mod4"
mod1 = "alt"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "k", lazy.layout.down()),
    ([mod], "Down", lazy.layout.down()),
    ([mod], "i", lazy.layout.up()),
    ([mod], "Up", lazy.layout.up()),
    ([mod], "j", lazy.layout.left()),
    ([mod], "Left", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "Right", lazy.layout.right()),

    # Resize windows (MonadTall/MonadWide)
    ([mod, "shift"], "d", lazy.layout.grow()),
    ([mod, "shift"], "a", lazy.layout.shrink()),

    # Layouts
    ([mod, "shift"], "f", lazy.window.toggle_floating()), # Cambia al layout flotante
    ([mod, "shift"], "Up", lazy.window.toggle_fullscreen()), # Cambia a pantalla completa

    # Move windows up or down in current stack
    ([mod, "shift"], "i", lazy.layout.shuffle_down()),
    ([mod, "control"], "Up", lazy.layout.shuffle_down()),
    ([mod, "control"], "Down", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod, "control"], "d", lazy.next_layout()),
    ([mod, "control"], "a", lazy.prev_layout()),
    ([mod, "control"], "Right", lazy.next_layout()),
    ([mod, "control"], "Left", lazy.prev_layout()),

    # Kill window
    ([mod], "q", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "x", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod], "Tab", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("vivaldi-stable")),

    # File Explorer
    ([mod], "f", lazy.spawn("nautilus")),

    # Discord
    ([mod], "d", lazy.spawn("discord")),

    # Spotify
    ([mod], "p", lazy.spawn("flatpak run com.spotify.Client")),

    # Signal
    ([mod], "m", lazy.spawn("flatpak run org.signal.Signal")),

    # Terminal
    ([mod], "t", lazy.spawn("kitty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),
    ([], "Print", lazy.spawn("scrot")),
    (['mod1'], "Print", lazy.spawn("scrot -s")),

    # Calculadora
    ([], "XF86Calculator", lazy.spawn('gnome-calculator')),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5")),

    ([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5")),

    ([], "XF86AudioMute", lazy.spawn("pamixer -t")),

    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),

    # Hotkeys - TeteBD
    (['mod1'], "a", lazy.spawn('shutdown now')), # Apaga la computadora
    (['mod1'], "r", lazy.spawn('reboot')), # Reincicia la computadora
    ([mod], "l", lazy.spawn('betterlockscreen -l blur -- -u')), # Bloquea la pantalla
    (['mod1'], "m", lazy.spawn("kitty -e alsamixer")), # Abre alsamixer

    # Ventanas - TeteBD
    ([mod, "shift"], "Right", lazy.layout.next()), # Cambia a la siguiente ventana en el mismo grupo.
    ([mod, 'mod1'], "d", lazy.screen.next_group()),
    ([mod, "mod1"], "a", lazy.screen.prev_group()),
    ([mod, "mod1"], "Right", lazy.screen.next_group()),
    ([mod, "mod1"], "Left", lazy.screen.prev_group()),

    # Brightness
    #([mod], "", lazy.spawn("brightnessctl set +10%")),
    #([mod], "", lazy.spawn("brightnessctl set 10%-")),
]]
