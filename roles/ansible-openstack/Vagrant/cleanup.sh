#!/bin/bash
vagrant destroy -f
if [ -d .vagrant ]; then
  rm -rf .vagrant
fi
for file in *.retry; do
  if [[ -f $file ]]; then
    rm $file
  fi
done
