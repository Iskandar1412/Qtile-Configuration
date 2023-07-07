# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import psutil
import subprocess
from libqtile import hook

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import base, WindowName


# ------------KEYS------------
mod = "mod4"
terminal = guess_terminal()


keys = [
    # ------------ Window Configs ------------

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Terminal
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # ------------ App Config ------------

    # Comandos para menu rofi
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Abrir Menu"),
    
    # Comandos para lanzar aplicaciones
    # Firefox
    Key([mod], "f", lazy.spawn("firefox"), desc="Abrir Firefox"),
    
    # Vivaldi
    Key([mod], "v", lazy.spawn("vivaldi-stable"), desc="Abrir Vivaldi"),
    
    # Thunar (explorador de archivos)
    Key([mod], "a", lazy.spawn("thunar"), desc="Explorer"),

    # Gitkraken
    Key([mod], 'g', lazy.spawn("gitkraken"), desc="Open GitKraken"),

    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    
    #Bright
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    

    # ------------ Config Key ------------
    Key([mod], "p", lazy.spawn("code /home/iskandar/.config/qtile/config.py"), desc="Edit Keys"),

    # ------------ Config Captures ------------
    Key([mod], "s", lazy.spawn("scrot"), desc="Captura"),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s"), desc="Capturas"),
    
]


# ------------GROUPS------------ 
#Pagina: https://www.nerdfonts.com/cheat-sheet

#Listado Iconos Arch Linux

#1. nf-linux-archlinux
#2. nf-md-google_chrome
#3. nf-oct-terminal
#4. nf-dev-code_badge
#5. nf-md-microsoft_visual_studio_code
#6. nf-fa-code_fork  
#6.1. nf-dev-git_merge  
#7. nf-md-star_crescent
#8. nf-seti-config
#9. nf-fa-sitemap

groups = [Group(i) for i in [
    "  ", " 󰊯 ", "  ", "  ", " 󰨞 ", "  ", " 󰥹 ", "  ", "  ",
]]

for i, group in enumerate(groups):
    numeroEscitorio = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numeroEscitorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscitorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# ------------LAYOUTS------------

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# ------------WIDGETS------------

widget_defaults = dict(
    font="Shure Tech Mono Nerd Font",
    fontsize=17,
    padding=1,
)
extension_defaults = widget_defaults.copy()

# ------------SCREENS------------

# nf-ple-left_half_circle_thick 
# nf-ple-right_half_circle_thick 
# nf-fa-square 
# nf-cod-triangle_left 
# Función para las abridas y cerradas de los circulos             
def func_pest(vColor, tipo):
    if tipo == 0:
        icono = "" # nf-ple-left_half_circle_thick
        return widget.TextBox(
            text = icono,
            fontsize=25,
            padding=-6.5,
            margin=0,
            foreground=vColor,
            background="#282A36"
        )
    else:
        icono = "" # nf-ple-right_half_circle_thick
        return widget.TextBox(
            text = icono,
            fontsize=25,
            padding=-11,
            margin=0,
            foreground=vColor,
            background="#282A36"
        )

def func_icon(icono, color, background):
    return widget.TextBox(
        text = icono,
        padding=0,
        margin=0,
        background=background,
        foreground=color,
        fontsize=18
    )

# nf-md-pac_man 󰮯
# nf-md-all_inclusive_box_out 󱢎
# nf-md-circle_expand 󰺖

def separator():
    return widget.Sep(linewidth=0, padding=4)

# Interfaz red
disp_red = 'wlp3s0'

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.GroupBox(
                    active="#1C7DB1",
                    other_current_screen_border="#1C7DB1",
                    this_current_screen_border="#1C7DB1",
                    borderwidth=0,
                    inactive="#B22208",
                    ohter_screen_border="#B22208",
                    this_screen_border="#B22208",
                    #background="#ffffff",
                    padding=3,
                    highlight_method = 'block',
                    block_highlight_text_color="#ffffff",
                ),
                #widget.Prompt(),
                separator(),
                widget.WindowName(
                    #background="#ffffff",
                    foreground="#1C7DB1",
                    fontsize=12,
                    padding=12,
                    format="{name}",
                    #max_chars=65,
                ),
                separator(),
                #widget.Chord(
                #    
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(
                    icon_size = 20,
                ),
                separator(),
                
                # -----------GROUPS-----------
                # G1
                func_pest('#ffffff', 0),
                func_icon(' ', "#000000", '#ffffff'), # nf-fa-thermometer_half 
                widget.ThermalSensor(
                    foreground="#000000",
                    padding=2,
                    background="#ffffff",
                    threshold=50,
                    fontsize=14,
                    tag_sensor="Core 0",
                    fmt='T1: {}',
                ),
                func_icon('   ', '#B22208', "#ffffff"), # nf-fa-save
                widget.Memory(
                    foreground="#B22208",
                    background="#ffffff",
                    fontsize=14,
                ),
                func_pest('#ffffff', 1),

                # G2
                #separator(),
                func_pest('#B22208', 0),
                # nf-fa-refresh 
                func_icon('  ', '#282A36', '#B22208'),
                widget.CheckUpdates(
                    background="#B22208",
                    colour_have_updates="#282A36",
                    colour_no_updates="#282A36",
                    no_update_string='0',
                    display_format='Updates: {updates}',
                    update_interval=1800, #En segundos es el intervalo
                    distro='Arch_checkupdates',
                ),
                # nf-md-speedometer 󰓅
                func_icon(' 󰓅 ', '#282A36', '#B22208'),
                widget.Net(
                    # nf-oct-arrow_up 
                    # nf-oct-arrow_down 
                    # nf-fa-arrow_circle_up 
                    # nf-fa-arrow_circle_dow 
                    foreground="#282A36",
                    background="#B22208",
                    format='{down}   {up}',
                    interface=disp_red,
                    fontsize=14,
                    use_bits='true'
                ),
                func_pest('#B22208', 1),

                # G3
                func_pest('#1C7DB1', 0),
                widget.Clock(
                    format="%d/%m/%Y %A %H:%M:%S",
                    background="#1C7DB1",
                    foreground="#ffffff",
                    fontsize=14,
                ),
                # nf-fa-volume_up 
                func_icon('   ', '#282A36', '#1C7DB1'),
                widget.PulseVolume(
                    foreground="#000000",
                    background="#1C7DB1",
                    fontsize=14,
                    limit_max_volume=True,

                ),
                func_pest('#1C7DB1', 1),
                func_pest('#9E1F9B', 0),
                widget.CurrentLayoutIcon(
                    background="#9E1F9B",
                    foreground="#ffffff",
                    scale=0.7
                ),
                widget.CurrentLayout(
                    background="#9E1F9B",
                    fontsize=0,
                ),
                func_pest('#9E1F9B', 1),

                #widget.QuickExit(),
            ],
            24, #Tamaño de la barra
            # background="#1E20AD",
            background="#282A36",
            
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# ------------MOUSE------------

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


# ------------GENERAL------------

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
