
@echo off
rem -------------------------------------
if not "%~1"=="p" start /min cmd.exe /c %0 p&exit
rem -------------------------------------
cd /d "%~dp0"
set "TOPDIR=%cd%"
title "%~n0"
rem -------------------------------------
if "x%WBK_ROOTDIR%" == "x"      set "    WBK_ROOTDIR=D:/wbk"
if "x%PGM_ROOTDIR%" == "x"      set "    PGM_ROOTDIR=D:/pgm"
if "x%PGMBAK_ROOTDIR%" == "x"   set " PGMBAK_ROOTDIR=E:/pgm"
if "x%PGMBAK2_ROOTDIR%" == "x"  set "PGMBAK2_ROOTDIR=F:/pgm"
rem -------------------------------------

rem -------------------------------------
: setlocal enabledelayedexpansion
rem -------------------------------------
setlocal enabledelayedexpansion
rem -------------------------------------


rem -------------------------------------
set "ORIGIN_PATH=%PATH%"
set "MINI_PATH=C:/WINDOWS/system32;C:/WINDOWS;C:/WINDOWS/System32/Wbem"
set "PATH=%MINI_PATH%"
rem -------------------------------------

rem -------------------------------------
set "MINICONDA_VER=3"
if "x1" == "x1" call "%WBK_ROOTDIR%/etc/skel/tpl.tools.env.Miniconda.bat"
if "x12" == "x1" (
set "MINICONDA_TOPDIR=!PGM_ROOTDIR!/DEV/Miniconda/Miniconda2/x64/envs/envWbkPy2"
set "MINICONDA_ROOTDIR=!MINICONDA_TOPDIR!"

set "PATH=!MINICONDA_ROOTDIR!;!MINICONDA_ROOTDIR!/Scripts;!PATH!"
)
rem -------------------------------------

rem -------------------------------------
echo [pyExcel2Pads] - Installing local dev ...
rem -------------------------------------

pip install -e . >%~n0.log 2>&1

rem goto :eof_with_pause
if "%errorlevel%" == "0" goto :eof_with_exit
rem -------------------------------------
:eof_with_pause
pause
:eof_with_exit
goto :eof
