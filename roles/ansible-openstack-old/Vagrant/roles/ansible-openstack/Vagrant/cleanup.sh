#!/bin/bash
vagrant destroy -f
if [ -d .vagrant ]; then
  rm -rf .vagrant
fi
