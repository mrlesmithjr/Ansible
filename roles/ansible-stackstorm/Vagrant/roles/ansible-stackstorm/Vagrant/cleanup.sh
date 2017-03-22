#!/bin/bash
vagrant destroy -f
if [ -d host_vars ]; then
  rm -rf host_vars
fi
if [ -d .vagrant ]; then
  rm -rf .vagrant
fi
