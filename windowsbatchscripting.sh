@echo off
rem Turns off the echoing of commands in the batch script.

setlocal enabledelayedexpansion
rem Enables delayed variable expansion

set /p sourcePath=Enter the source folder path:
rem Prompts the user to enter the path of the source folder

set /p destinationPath=Enter the destination folder path:
rem Prompts the user to enter the path of the destination folder 

if not exist "!sourcePath!\" (
    echo Error: Source folder does not exist.
    goto :eof
)
rem Checks if the source folder exist, shows error if it doesnt 

if not exist "!destinationPath!\" (
    echo Error: Destination folder does not exist.
    goto :eof
)
rem Checks if the destination folder exists, shows error message if it doesnt

robocopy "!sourcePath!" "!destinationPath!" /E
rem Uses the robocopy command to copy source folder contents to the destination

if errorlevel 8 (
    echo Error: ROBOCOPY encountered errors during the copy operation.
) else (
    echo Copy operation completed successfully.
)
rem Check if Robocopy encountered errors during the copy operation 

:end
endlocal
rem end of scrimt, and clean of local enviorment

