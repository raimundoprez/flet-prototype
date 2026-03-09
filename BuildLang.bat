:: make sure you have installed msgfmt before running this script! it is required to compile the language files.

@echo off
setlocal enabledelayedexpansion

:: directory that contains the language directories
set "dir=resource\locale"

:: scan each language directory
for /d %%d in ("%dir%\*") do (
	if exist "%%d\LC_MESSAGES" (
		echo Scanning directory: %%d
		
        :: scan each language file for the language given
		for %%p in ("%%d\LC_MESSAGES\*.po") do (
			echo Compiling file: %%p
			
			set "po_file=%%~nxp"
			set "mo_file=%%d\LC_MESSAGES\!po_file:.po=.mo!"
			
            :: compile .po into .mo
			msgfmt "%%p" -o "!mo_file!"
		)
		
		echo.
	)
)

pause