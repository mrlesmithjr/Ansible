vagrant destroy -f
if exist "host_vars" rmdir /S /Q host_vars
if exist ".vagrant" rmdir /S /Q .vagrant
