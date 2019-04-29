
@echo off
rem -------------------------------------
if not "%~1"=="p" start /min cmd.exe /c %0 p&exit
rem -------------------------------------
cd /d "%~dp0"
set "TOPDIR=%cd%"
title "%~n0"
rem -------------------------------------
if "x%PGM_ROOTDIR%" == "x"  set "  PGM_ROOTDIR=D:/pgm"
if "x%WBK_ROOTDIR%" == "x"  set "WBK_ROOTDIR=D:/wbk"
rem -------------------------------------

rem -------------------------------------
: setlocal enabledelayedexpansion
rem -------------------------------------
setlocal enabledelayedexpansion
rem -------------------------------------


:----------------------------------------
set "ORIGIN_PATH=%PATH%"
set "MINI_PATH=C:/WINDOWS/system32;C:/WINDOWS;C:/WINDOWS/System32/Wbem"
set "PATH=%MINI_PATH%"
:----------------------------------------

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
echo [pyEdaBomHelper] - running tests...
rem -------------------------------------

call :fun_getProjectNameByShellName
set "_SHELLFN_PATCH=pads-test1"

set "SCRIPT_ROOTDIR=!TOPDIR!"

set "PROJECT_ROOTDIR=!SCRIPT_ROOTDIR!/Examples"
set "ACTION_SRCDIR=!PROJECT_ROOTDIR!/!_SHELLFN_PATCH!"
set "ACTION_DSTDIR=!PROJECT_ROOTDIR!"

if "x1" == "x1" (
call pyExcel2Pads -i !ACTION_SRCDIR! ^
		           -o !ACTION_DSTDIR!/ ^
		           -v ^
		           >!ACTION_DSTDIR!/!_SHELLFN_PATCH!.convert.log 2>&1
)

rem goto :eof_with_pause
if "%errorlevel%" == "0" goto :eof_with_exit
rem -------------------------------------
:eof_with_pause
pause
:eof_with_exit
goto :eof

:fun_getProjectNameByShellName
rem -------------------------------------
rem ex: ACTION-PRJNAME.bat
set "_SHELL_FILE_NAME=%~n0"
set "_SHELL_FILE=!_SHELL_FILE_NAME:~12!"
set "_SHELL_FILE=!_SHELL_FILE_NAME!"
rem for /f "tokens=x,y,m-n delims=chars" %%a in ("str")   do cmd
for /f "tokens=1,2* delims=-" %%a in ("!_SHELL_FILE!") do (
	set "_SHELLFN_MAJOR=%%a"
	set "_SHELLFN_MINOR=%%b"
	set "_SHELLFN_PATCH=%%c"
)
set "_SHELLFN_MAJOR=!_SHELLFN_MAJOR:#=-!"
echo [Debug] [_SHELLFN_MAJOR=!_SHELLFN_MAJOR!] - [_SHELLFN_MINOR=!_SHELLFN_MINOR!] - [_SHELLFN_PATCH=!_SHELLFN_PATCH!]
goto :eof
rem -------------------------------------
