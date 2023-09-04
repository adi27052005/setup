#!/bin/bash 

conky -c $HOME/.config/conky/conky.config &
# nitrogen --restore &
# xsetroot -name "Aditya Gautam EVE 23043"
# emacs $HOME/college_stuff.org
#/usr/bin/emacs --daemon
xautolock -notifier "notify-send 'Locking in 30 seconds!'" -notify 30 -locker "i3lock --color 111111 --show-failed-attempts" -time 5 &
# if [[ "$(cat $HOME/theme.txt)"=="blue" ]]; then nitrogen --set-zoom-fill $HOME/wallpaper/blue.jpg; elif [[ "$(cat $HOME/theme.txt)"=="purple" ]]; then nitrogen --set-zoom-fill $HOME/wallpaper/purple.jpg; fi
nitrogen --set-zoom-fill "$(cat $HOME/wallpaper.txt)"

picom --animations --animation-window-mass 0.5 --animation-for-open-window zoom --animation-stiffness 200 -c &
while true; do xsetroot -name " 9717166477    Aditya Gautam EVE 2023043     $(acpi | cut -d ':' -f2-)    $(date '+%I:%M %p | %B %d, %Y: %A')"; sleep 1m; done
