@echo off
pybot	--timestampoutputs --outputdir=ResultFiles ^
	--loglevel=TRACE ^
	-i Login ^
	%*
pause
