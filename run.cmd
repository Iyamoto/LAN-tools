@echo off
psexec \\%1 -cf autorunsc.exe -accepteula -s -c -m > cache\%1.csv
rem type rez.csv >> rez2.csv
rem cat rez2.csv