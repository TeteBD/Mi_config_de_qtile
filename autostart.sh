#!/bin/sh

# systray battery icon
# cbatticon -u 5 & Para laptops
# systray volume
# volumeicon &

# Custom
redshift -O 2400 # Protección visual, instala redshift.
feh --bg-fill ~/.config/qtile/res/images/background.png # Poner la ruta a la imágen que se usará como fondo de pantalla.
xautolock -time 5 -locker 'betterlockscreen -l blur -- -u' & # Instalar betterlockscreen y xautolock configurarlo.
picom & # Trasparencias
volctl &
numlockx on
