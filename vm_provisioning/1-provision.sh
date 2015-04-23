#!/bin/bash
playbook_dir=./playbooks
playbook_file=provision.yml
host_inventory=provision_hosts
current_dir=$(pwd)
datestamp=$(date +%Y%m%d_%H%M%S)
backup_folder=./backups

if [[ ! -e $backup_folder ]]; then
  mkdir $backup_folder
fi

# Backup currently $playbook_file
cp $playbook_dir/$playbook_file $backup_folder/$playbook_file.$datestamp
cp $playbook_dir/$playbook_file $backup_folder/$playbook_file.backup

# Execute provisioning playbook
ansible-playbook -i $host_inventory $playbook_dir/$playbook_file

# Restore original $playbook_file
mv $backup_folder/$playbook_file.backup $playbook_dir/$playbook_file
