from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

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
        text="", # Icon: nf-oct-triangle_left
        fontsize=25,
        padding=-7
    )

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
            padding_x=2,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['active'],
            this_screen_border=colors['inactive'],
            other_current_screen_border=colors['active'],
            other_screen_border=colors['inactive'],
            block_highlight_text_color="#ffffff",
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='active'), fontsize=13, padding=5),
        separator(),
    ]

primary_widgets = [
    *workspaces(),
    separator(),
    
    powerline('color7', 'dark'),
    icon(bg="color7", text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(
        background=colors['color7'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),
    
    powerline('color6', 'color7'),
    icon(bg="color6", text=' ', fg="color_white"),  # Icon: nf-fa-feed
    widget.Net(**base(bg='color6', fg="color_white"), interface='wlp3s0', format=('{down} ↓↑ {up}'),use_bits='true'),
    
    powerline('color5', 'color6'),
    icon(bg="color5", text='󰍛', fg="color_white"), # Icon: nf-md-memory
    widget.Memory(**base(bg='color5', fg="color_white")),

    powerline('color4', 'color5'),
    widget.CurrentLayoutIcon(**base(bg='color4'), scale=0.65),
    #widget.CurrentLayout(fontsize=0),
    
    powerline('color3', 'color4'),
    icon(bg="color3", fontsize=15, text=' ', fg="color_white"), # Icon: nf-cod-calendar
    widget.Clock(**base(bg='color3', fg="color_white"), format='%d/%m %A %H:%M:%S'),
    
    powerline('color2', 'color3'),
    icon(bg="color2", text='󱊢', fg="color_white"), # Icon: nf-md-battery_medium
    widget.Battery(**base(bg="color2", fg="color_white"), format="{percent:2.0%}"),
    icon(bg="color2", text=' ', fg="color_white"), # Icon: nf-fa-volume_up 
    widget.PulseVolume(**base('color_white', 'color2'), limit_max_volume=True),
    
    powerline('color1', 'color2'),
    widget.Systray(background=colors['color1'],  padding=5),
]

secondary_widgets = [
    *workspaces(),
    separator(),
    powerline('color1', 'dark'),
    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
    #widget.CurrentLayout(**base(bg='color1'), padding=5, fontsize=0),
    powerline('color2', 'color1'),
    widget.Clock(**base(bg='color1'), format='%d/%m %A %H:%M:%S'),
    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()