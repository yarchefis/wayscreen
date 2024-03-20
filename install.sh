#!/bin/bash

# Check package manager and install pip accordingly
if command -v apt &> /dev/null; then
    sudo apt update
    sudo apt install -y python3-pip
elif command -v pacman &> /dev/null; then
    sudo pacman -Sy
    sudo pacman -S --noconfirm python-pip
else
    echo "Error: Unsupported package manager"
    exit 1
fi

mkdir download-wayscreen

python3 -m venv download-wayscreen
source download-wayscreen/bin/activate

mv wayscreen/* download-wayscreen/



pip install pyinstaller pyscreenshot pillow
PYINSTALLER_PATH=$(which pyinstaller)
cd download-wayscreen || exit
"$PYINSTALLER_PATH" --onefile main.py

cd dist || exit
mv main wayscreen
chmod +x wayscreen

if command -v sudo &> /dev/null; then
    sudo cp wayscreen /bin/
    echo "The program has been successfully installed! Thank you for choosing us, more cool projects on the website https://yarchefis.ru"
    deactivate
    sudo rm -rf download-wayscreen
    sudo rm -rf wayscreen
elif command -v doas &> /dev/null; then
    doas cp wayscreen /bin/
    echo "The program has been successfully installed! Thank you for choosing us, more cool projects on the website https://yarchefis.ru"
    deactivate
    doas rm -rf download-wayscreen
    doas rm -rf wayscreen
else
    echo "There was an error installing the program in /bin. Make sure you have sudo or doas"
fi
