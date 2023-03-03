@echo OFF
title mosi-sol checksum
color 0A
echo "----------checksum----------"
echo this is the source of checksum (windows version), use on my archived/finalize repositories for validate download.
echo github is safe by check own checksum, but i add this just for case!

:: source create
for /r %%f in (*) do (certutil -hashfile "%%f" MD5 | find /v "hash") >> checksum.md 

::validate create
::for /r %%f in (*) do (certutil -hashfile "%%f" MD5 | find /v "hash") >> output.dat

echo validate your download by checksum.md , check in output.dat 
pause 
exit /b