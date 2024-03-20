# wayscreen - A simple screenshot program running under Wayland

![Alt text](https://yarchefis.ru/static/img/wayscreen.png)

## about
This program takes screenshots of the entire screen or a selected area under Wayland.
Wayland has great limitations when it comes to screen capture (video recording, streams, etc.)

program website (Russian) - https://yarchefis.ru/wayscreen

## usage
- wayscreen - open menu
- wayscreen path - change the path where screenshots are stored
- wayscreen full - take a screenshot of the entire screen
- wayscreen area - take a screenshot of the area

## install
### debian/ubuntu and Arch Linux/Manjaro:
clone the repository
go to folder
run `chmod +x install.sh`
run `./install.sh` and wait with a cup of tea
after installation you can use `wayscreen`

### windows may not work! the code is written for Linux:
clone the repository. Install the necessary packages (python3, pip, pillow, tkinter, pyinstaller)
run `pyinstaller --onefile main.py`
your exe will be in the `dist` folder
