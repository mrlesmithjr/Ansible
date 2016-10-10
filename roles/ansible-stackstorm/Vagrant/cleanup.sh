#!/usr/bin/env bash
vagrant destroy -f
for file in *.retry; do
  if [[ -f $file ]]; then
    rm $file
  fi
done
if [ -d host_vars ]; then
  rm -rf host_vars
fi
if [ -d .vagrant ]; then
  rm -rf .vagrant
fi
