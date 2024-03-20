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

mv area_capture.py full_capture.py main.py screen_capture.py download-wayscreen/



pip install pyinstaller pyscreenshot pillow
PYINSTALLER_PATH=$(which pyinstaller)
cd download-wayscreen || exit
"$PYINSTALLER_PATH" --onefile main.py

cd dist || exit
chmod +x main
echo "main in place. I issue right"

if command -v sudo &> /dev/null; then
    sudo cp main /bin/
    sudo mv /bin/main /bin/wayscreen
    echo "The program has been successfully installed! Thank you for choosing us, more cool projects on the website https://yarchefis.ru"
    deactivate
elif command -v doas &> /dev/null; then
    doas cp main /bin/
    doas mv /bin/main /bin/wayscreen
    echo "The program has been successfully installed! Thank you for choosing us, more cool projects on the website https://yarchefis.ru"
    deactivate
else
    echo "There was an error installing the program in /bin. Make sure you have sudo or doas"
fi
