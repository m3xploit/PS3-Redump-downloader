# PS3-Redump-downloader v1.00

A LITERAL clone of PS2-Redump-downloader for PlayStation 3 ROMs.

The PS3RD is a Python-based utility that allows users to search for and download PlayStation 3 (PS3) ROMs directly from the Myrient repository. It provides a user-friendly command-line interface with progress indicators for seamless downloading.

Note: It was designed for running on windows but there shouldn't be any problems when running on UNIX based systems, except the compiling part. On UNIX based system, just run it using python main.py

## Compiling:

Before compiling make sure you got python3 and pip3 installed on your system!

On windows you can install PS3RD by executing the build.bat script provided.
You can also manually compile it using these commands:
```
Microsoft Windows [Version 10.0.22631.4974]
(c) Microsoft Corporation. Alle Rechte vorbehalten.

C:\Users\user1> python -m pip install -r requirements.txt
C:\Users\user1> pyinstaller main.py --console --noconfirm --onefile --icon icon.ico
```
