@echo off
cd %~dp0
echo _______________________________________________ >> log.txt
:start:
echo starting at %time% the %date% >> log.txt
main.py
echo Crashed at %time% the %date% >> log.txt
echo restarting... >> log.txt
goto start