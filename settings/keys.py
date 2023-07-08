
from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"


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

    # Code
    Key([mod], 'p', lazy.spawn("code"), desc="Open VSCode"),

    # ------------ Hardware Configs ------------

    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    
    #Bright
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),
    

    # ------------ Config Key ------------
    Key([mod], "e", lazy.spawn("code /home/iskandar/.config/qtile/settings/keys.py"), desc="Edit Keys"),

    # ------------ Config Captures ------------
    Key([mod], "s", lazy.spawn("scrot"), desc="Captura"),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s"), desc="Capturas"),
     
    # ------------ Maximize & Minimize ------------
    Key([mod], "z", lazy.window.toggle_minimize(), desc="Restore minimized window & Minimize"),

]
