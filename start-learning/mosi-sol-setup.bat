::Mosi-Sol from github - learning solidity
::windows users version
@echo OFF
title https://github.com/mosi-sol
color 0A

echo "batch file for windows, unix  need bash file to run!"
echo "if your (git) installed, continue! else [ ctrl+c ] to exit"
echo "Tips: put this file (mosi-sol-setup.bat) into an empty folder, then run script"
echo .
goto :setter

:setter
set /p SETSEOSONs="Season 1, 2, 3, 4 (or 0 for exit): "
set /A SETSEOSON=%SETSEOSONs%
goto :conditions


:conditions
    if %SETSEOSON%==1 (goto :season1)
    if %SETSEOSON%==2 (goto :season2)
    if %SETSEOSON%==3 (goto :season3)
    if %SETSEOSON%==4 (goto :season4)
    if %SETSEOSON%==0 (goto :theend)
    if %SETSEOSON% NEQ 0 || %SETSEOSON% NEQ 1 || %SETSEOSON% NEQ 2 || %SETSEOSON% NEQ 3 || %SETSEOSON% NEQ 4 (goto :theend)
    @REM 5 or other char or letter or word just close program!
EXIT /B %ERRORLEVEL%

:season1
    echo "Season 1 ready to download" 
    git clone https://github.com/mosi-sol/live-contracts.git
    echo ___________________________
    pause 
call :setter
::exit /b 0

:season2
    echo "Season 2 ready to download" 
    git clone https://github.com/mosi-sol/live-contracts-s2.git
    echo ___________________________
    pause
goto :setter


:season3
    echo "Season 3 ready to download" 
    git clone https://github.com/mosi-sol/live-contract-s3.git
    echo ___________________________
    pause
goto :setter


:season4
    echo "Season 4 ready to download" 
    git clone https://github.com/mosi-sol/live-contracts-s4.git
    echo ___________________________
    pause
goto :setter


:theend
color 08
echo    ************
echo    * GOODLUCK *
echo    ************
pause 
exit 
