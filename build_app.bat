@echo off
call .qtcreator/Scripts/activate
echo Building started
pyinstaller --clean --onefile --icon=icon.ico --windowed --add-binary ".\ffmpeg.exe;." --add-data "src/img/no_connection.png;img" --add-data "src/img/connection_established.png;img" --add-data "resources/lang/ru.json;resources/lang" --add-data "resources/lang/en.json;resources/lang" --hidden-import 'zeroconf._utils.ipaddress' --hidden-import 'zeroconf._handlers.answers' -w main.py
rename .\dist\main.exe client_with_new_ffmpeg.exe
echo Build was successful
