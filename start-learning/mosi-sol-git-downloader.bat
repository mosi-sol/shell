::Mosi-Sol from github - learning solidity
::windows users version
@echo OFF
title https://github.com/mosi-sol
color 0A

echo "batch file for windows, unix  need shell-script to run!"
echo "if your (git) installed, continue! else [ ctrl+c ] to exit"
echo "Tips: put this file ( .bat ) into an empty folder, then run script"
echo .
goto :setter

:setter
set /p SETSEOSONs="All github repositories"
set /A SETSEOSON=%SETSEOSONs%
goto :season1

:season1
    echo "download start" 
    echo ___________________________
	echo --------- mosi-sol -----------
	echo ===================================
    git clone https://github.com/mosi-sol/shell.git
	echo ===================================
    git clone https://github.com/mosi-sol/live-contracts-s4.git
	echo ===================================
    git clone https://github.com/mosi-sol/live-contract-s3.git
	echo ===================================
    git clone https://github.com/mosi-sol/live-contracts-s2.git
	echo ===================================
    git clone https://github.com/mosi-sol/live-contracts.git
	echo ===================================
    git clone https://github.com/mosi-sol/erc20.git
	echo ===================================
    git clone https://github.com/mosi-sol/VerifySignature.git
	echo ===================================
    git clone https://github.com/mosi-sol/5min.git
	echo ===================================
    git clone https://github.com/mosi-sol/proof.git
	echo ===================================
    git clone https://github.com/mosi-sol/Wallet-Web3.git
	echo ===================================
    git clone https://github.com/mosi-sol/NftWallet.git
	echo ===================================
    git clone https://github.com/mosi-sol/audit.git
	echo ===================================
    git clone https://github.com/mosi-sol/ERC20-Dapp.git
	echo ===================================
    git clone https://github.com/mosi-sol/incoterms.git
	echo ===================================
    git clone https://github.com/mosi-sol/startup.git
	echo ===================================
    git clone https://github.com/mosi-sol/Election.git
	echo ===================================
    git clone https://github.com/mosi-sol/DNews.git
	echo ===================================
    git clone https://github.com/mosi-sol/blockchain-developers-idea.git
	echo ===================================
    git clone https://github.com/mosi-sol/gist.git	
    echo ___________________________
	pause
    echo "download finish"
    pause 
call :theend
::exit /b 0


:theend
color 08
echo    ************
echo    * GOODLUCK *
echo    ************
pause 
exit 