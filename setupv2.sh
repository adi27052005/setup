#!/bin/bash

paru -S xorg neovim-nightly-bin firefox kitty git nitrogen picom fm6000 polybar zsh i3-wm i3status i3lock xclip scrot ttf-jetbrains-mono-nerd ttf-fira-sans lsd npm nodejs unzip libnotify dunst bluez bluez-utils lxappearance-gtk3 btop cava gpick thunar imagemagick usbutils mtpfs jmtpfs gvfs-mtp gvfs-photo2 tldr playerctl breeze-obsidian-cursor-theme tlp guvcview ly flat-remix-gtk conky fd jdk17-openjdk ngrok wget zip nvidia nvidia-utils nvidia-settings envycontrol openssh ttf-quicksand-variable acpi ybacklight xbindkeys

sudo systemctl enable ly
sudo systemctl enable bluetooth

git clone https://git.suckless.org/dmenu
cd $HOME/.config/dmenu
sudo make install
cd ~

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

printf '\n\n\n\nPut this in\n/etc/X11/xorg.conf.d/30-touchpad.conf\n\nSection "InputClass"
    Identifier "touchpad"
    Driver "libinput"
    MatchIsTouchpad "on"
    Option "Tapping" "on"
    Option "TappingButtonMap" "lmr"
    Option "NaturalScrolling" "true"
EndSection'

printf '\n\n\n\nPut this in\n/etc/sudoers\n\nadi ALL=NOPASSWD: /sbin/reboot, /sbin/poweroff\n\n'
