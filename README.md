# Qtile

## Instalación (Arch)

Instala qtile y dependencias:

```
- 1 pamixer
- 2 scrot
- 3 betterlockscreen
- 4 kitty
- 5 redshift
- 6 gnome-calculator
- 7 nautilus
- 8 volctl
- 9 xautolock
- 10 feh
- 11 numlockx
- 12 rofi
- 13 picom
- 14 dunst
```

Clona este repositorio y copia mis configuraciones:

```bash
git clone https://github.com/TeteBD/Mi_config_de_qtile.git ~/.config/qtile;bash ~/.config/qtile/autoQtile
```

Cuando todo este listo puedes iniciar sesión con Qtie. Pero los atajos de teclaco no funcionarán si no tienes los mismos programas y configuraciones que yo, puedes cambiar los atajos de teclado o instalar los programas y configuraciones que uso. En keys.py puedes ver y cambiar los atajos de teclado.

## Temas

Los temas se almacenan en ```Themes``` Para usar un tema cambia ```./config.json```:

```json
{
    "theme": "material-ocean"
}
