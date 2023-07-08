from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 
# nf-linux-docker,
# nf-mdi-image, 
# nf-mdi-layers

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