
@echo off
pushd %~dp0
pyinstaller -n hd2_stratagem_asr -y -i media\icon.png -w source\__main__.py --onefile --noupx --clean -p .
echo the exe is at %~dp0dist\hd2_stratagem_asr.exe
