import subprocess
import time
import os

theme = subprocess.getoutput("echo \"Purple\nBlue\" | dmenu")

if theme.lower()=="purple":

    # terminal background
    os.system("sed -i 's/#1a1c2a/#0a0217/g' $HOME/.config/kitty/kitty.conf")

    # GTK theme
    os.system("sed -i 's/gtk-theme-name=Flat-Remix-GTK-Magenta-Dark-Solid/gtk-theme-name=Flat-Remix-GTK-Violet-Dark-Solid/g' $HOME/.config/gtk-3.0/settings.ini")

    # DWM colors
    os.system("sed -i 's/#191e2a/#0a0217/g' $HOME/.config/dwm/config.h")
    os.system("sed -i 's/#56b6c2/#a272f0/g' $HOME/.config/dwm/config.h")
    os.system("sed -i 's/#262e40/#15052e/g' $HOME/.config/dwm/config.h")

    #Conky
    os.system("sed -i 's/#56b6c2/#a272f0/g' $HOME/.config/conky/conky.config ")
    os.system("sed -i 's/#191e2a/#0a0217/g' $HOME/.config/conky/conky.config ")

    # Wallpaper
    # os.system("sed -i 's/blue.jpg/purple.jpg/g' $HOME/.config/nitrogen/bg-saved.cfg")
    # os.system("nitrogen --set-zoom-fill $HOME/wallpaper/purple.jpg")
    os.system("echo purple > $HOME/theme.txt")



elif theme.lower()=="blue":

    # terminal background
    os.system("sed -i 's/#0a0217/#1a1c2a/g' $HOME/.config/kitty/kitty.conf")

    # GTK theme
    os.system("sed -i 's/gtk-theme-name=Flat-Remix-GTK-Violet-Dark-Solid/gtk-theme-name=Flat-Remix-GTK-Magenta-Dark-Solid/g' $HOME/.config/gtk-3.0/settings.ini")

    # DWM colors
    os.system("sed -i 's/#0a0217/#191e2a/g' $HOME/.config/dwm/config.h")
    os.system("sed -i 's/#a272f0/#56b6c2/g' $HOME/.config/dwm/config.h")
    os.system("sed -i 's/#15052e/#262e40/g' $HOME/.config/dwm/config.h")

    # Conky
    os.system("sed -i 's/#a272f0/#56b6c2/g' $HOME/.config/conky/conky.config ")
    os.system("sed -i 's/#0a0217/#191e2a/g' $HOME/.config/conky/conky.config ")

    # Wallpaper
    # os.system("sed -i 's/purple.jpg/blue.jpg/g' $HOME/.config/nitrogen/bg-saved.cfg")
    # os.system("nitrogen --set-zoom-fill $HOME/wallpaper/blue.jpg")
    os.system("echo blue > $HOME/theme.txt")


os.system("cd $HOME/.config/dwm; sudo make clean install")
os.system("cd $HOME/.config/dmenu; sudo make clean install")
time.sleep(0.5)
os.system("killall dwm")
