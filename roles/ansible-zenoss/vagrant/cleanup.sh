#!/bin/bash
vagrant destroy -f
if [ -d host_vars ]; then
  rm -rf host_vars
fi
if [ -d .vagrant ]; then
  rm -rf .vagrant
fi
if [ -d roles ]; then
  rm -rf roles
fi
