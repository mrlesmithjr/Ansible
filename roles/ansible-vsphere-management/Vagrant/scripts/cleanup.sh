#!/bin/bash

####
# Beginning of script execution path detection
####
# SCRIPT_NAME=$0
SCRIPT_FULL_PATH=$(dirname "$0")
####
# End of script execution path detection
####

cd $SCRIPT_FULL_PATH/../
vagrant destroy -f
cd -
if [ -d $SCRIPT_FULL_PATH/../host_vars ]; then
  rm -rf $SCRIPT_FULL_PATH/../host_vars
fi
if [ -d $SCRIPT_FULL_PATH/../.vagrant ]; then
  rm -rf $SCRIPT_FULL_PATH/../.vagrant
fi
