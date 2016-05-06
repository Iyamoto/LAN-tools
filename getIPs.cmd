@echo off
net view | grep \\ | sed s/\\\\// | gawk "{print $1}" > tmp.txt 
for /f %%j in (tmp.txt) do ( ping %%j -l 1 -n 1 | find "TTL" > nul & if %ERRORLEVEL% neq 1 echo %%j >> online.txt )
for /f %%j in (online.txt) do ping %%j -l 1 -n 1 | grep %%j | gawk -F[ "{print $2}" | gawk -F] "{print $1}"  >> lan1.conf
sort lan1.conf | uniq > lan.conf
del online.txt lan1.conf tmp.txt