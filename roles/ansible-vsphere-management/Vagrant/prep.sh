#!/usr/bin/env bash

LINKS=(".gitignore" "ansible.cfg" \
  "bootstrap.yml" "cleanup.bat" "playbook.yml" \
"requirements.yml" "unit-test.sh" "Vagrantfile" "prep_host_vars.yml")
TOP_FOLDER_PATH="../.."
for i in "${LINKS[@]}"
do
  if [ -f "./$i" ]; then
    rm "./$i"
  fi
  if [ ! -L "./$i" ]; then
    ln -s $TOP_FOLDER_PATH/$i .
  fi
done
ln -sf .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory hosts
