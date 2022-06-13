from libqtile import widget
from libqtile.config import Drag, Click
from .theme import colors
import re
import subprocess
from libqtile import qtile
from libqtile.widget import base
import os


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

#### FUNCTIONS #####

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )

# TeteBD's powerline
def tetepower(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",
        fontsize=37,
        padding=-2
    )

#### Mouse callbacks functions - TeteBD ####

# Powermenu - TeteBD
def open_powermenu():
    qtile.cmd_spawn('powermenu')
def suspendQtile():
    qtile.cmd_spawn('systemctl suspend')

# CPU - TeteBD
def open_htop():
    qtile.cmd_spawn('kitty htop')

def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]

primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=60,
        custom_command='checkupdates',
    ),

    # Volumen - TeteBD
    # powerline('color3', 'color4'),
    # icon(bg="color3", text='  '),
    # widget.Volume(**base(bg='color3'), emoji='True', fmt='Vol: {}', device='default'),
    # powerline('color2', 'color3'),

    # Indicador de mayusculas y numeros - TeteBD
    # powerline('color1', 'color3'),
    # widget.CapsNumLockIndicator(**base(bg='color1'), update_interval=0.001),

    # Temperatura del CPU
    powerline('color3', 'color4'),
    icon(bg='color3', text=" "),
    widget.ThermalSensor(**base(bg='color3'), update_interval=0.001, tag_sensor='Package id 0'),

    #CPU - TeteBD
    powerline('color2', 'color3'),
    icon(bg='color2', text=' '),
    widget.CPU(**base(bg='color2'),
        update_interval=0.5,
        mouse_callbacks={'Button1': open_htop}),

    # RAM - TeteBD
    powerline('color1', 'color2'),
    widget.Memory(**base(bg='color1'), measure_mem='G', format='Ram:{MemUsed: .0f}{mm} de {MemTotal:.0f}{mm} '),

    # Layout actual - TeteBD
    powerline('color4', 'color1'),
    widget.CurrentLayoutIcon(**base(bg='color4'), scale=0.65),
    widget.CurrentLayout(**base(bg='color4'), padding=5),

    # Reloj - TeteBD
    powerline('color3', 'color4'),
    icon(bg="color3", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock
    widget.Clock(**base(bg='color3'), format='%a %d/%m/%y - %I:%M %p'),

    # Cerrar sesión - TeteBD -- Reemplazado por Powermenu.
    # powerline('color4', 'color1'),
    # widget.QuickExit(**base(bg='color4'), default_text=('  Salir '), countdown_format=' {} [x]  '),
    # powerline('dark', 'color4',),

    # Powermenu
    powerline('color2', 'color3'),
    widget.TextBox(**base(bg='color2'), text=" ",
        mouse_callbacks={'Button1': open_powermenu,
                         'Button3': suspendQtile}),

    # Widgets de apps - TeteBD
    powerline('color1', 'color2'),
    widget.WidgetBox(**base(bg='color1'), fontsize=15 , widgets=[
        widget.Systray(**base(bg='color1'), padding=5, icon_size=15),
        powerline('dark', 'color1'),
    ]),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'color4'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('color3', 'color4'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
