#!/bin/sh

# Configuracion Teclado
setxkbmap latam &

# Configuracion pantalla
xrandr --output eDP1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output HDMI1 --off --output VIRTUAL1 --off &

# Iconos del sistema

udiskie -t &

nm-applet &

volumeicon &

#cbatticon -u 5 &

# Fondo de escritorio
nitrogen --restore &
