
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