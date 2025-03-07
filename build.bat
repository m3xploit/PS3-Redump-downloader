@echo off

python -m pip install -r requirements.txt
pyinstaller main.py --console --noconfirm --onefile --icon icon.ico

pause