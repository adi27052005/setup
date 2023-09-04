import subprocess
import os
import time

theme = [
        {
            "Name": "Panther",
            "primary_bg": "#a272f0",
            "secondary_bg": "#0a0217",
            "primary_fg": "#000000",
            "secondary_fg": "#ffffff",
            "gtk_theme": "Flat-Remix-GTK-Violet-Dark-Solid",
            "wallpaper": "$HOME/wallpaper/purple.jpg"
         },
        {
            "Name": "Blue",
            "primary_bg": "#56b6c2",
            "secondary_bg": "#191e2a",
            "primary_fg": "#000000",
            "secondary_fg": "#ffffff",
            "gtk_theme": "Flat-Remix-GTK-Magenta-Dark-Solid",
            "wallpaper": "$HOME/wallpaper/blue.jpg"
            },
        {
            "Name": "Red",
            "primary_bg": "#df5b61",
            "secondary_bg": "#07112c",
            "primary_fg": "#000000",
            "secondary_fg": "#ffffff",
            "gtk_theme": "Flat-Remix-GTK-Magenta-Dark-Solid",
            "wallpaper": "$HOME/wallpaper/red.jpg"
            },
        ]

l=[]
for i in range(len(theme)):
    l.append(theme[i]['Name'])
cmd = "\n".join(l)

result = subprocess.Popen(["dmenu"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
selected_option, _ = result.communicate(input=cmd)

selected_theme = selected_option.strip()

for i in range(len(theme)):
    if selected_theme == theme[i]["Name"]:
        # Terminal
        os.system((f"sed -i 's/background #.*/background "+ (theme[i]["secondary_bg"])+ "/g' $HOME/.config/kitty/kitty.conf"))

        # GTK theme
        os.system("sed -i 's/gtk-theme-name=.*/gtk-theme-name="+ (theme[i]["gtk_theme"]) +"/g' $HOME/.config/gtk-3.0/settings.ini")

        # DWM colors
        os.system("sed -i 's/static const char col_gray1\[\]=\"#.*\";/static const char col_gray1\[\]=\""+(theme[i]["secondary_bg"])+"\";/g' $HOME/.config/dwm/config.h")
        os.system("sed -i 's/static const char col_cyan\[\]=\"#.*\";/static const char col_cyan\[\]=\""+(theme[i]["primary_bg"])+"\";/g' $HOME/.config/dwm/config.h")

        # Conky
        os.system("sed -i 's/\tcolor0 = \"#.*\",/\tcolor0 = \""+(theme[i]["primary_bg"])+"\",/g' $HOME/.config/conky/conky.config ")
        os.system("sed -i 's/\tdefault_color = \"#.*\",/\tdefault_color = \""+(theme[i]["primary_bg"])+"\",/g' $HOME/.config/conky/conky.config ")
        os.system("sed -i 's/\town_window_colour = \"#.*\",/\town_window_colour = \""+(theme[i]["secondary_bg"])+"\",/g' $HOME/.config/conky/conky.config")

        # Wallpaper
        os.system("echo "+(theme[i]["wallpaper"])+" > $HOME/wallpaper.txt")

os.system("cd $HOME/.config/dwm; sudo make clean install")
os.system("cd $HOME/.config/dmenu; sudo make clean install")
time.sleep(0.5)
os.system("killall dwm")
