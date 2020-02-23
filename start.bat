@echo off && setlocal enabledelayedexpansion

cd run

set pyexe=E:\project\ptip\project\PyToolsIP\include\python\python.exe
set mainfile=main.py
set buildfile=build.py

run.vbs %pyexe% %mainfile% %buildfile%