#!/bin/bash
playbook_dir=./playbooks
playbook_file=gather.yml
gather_inventory=provision_hosts
host_inventory=bootstrap_hosts
current_dir=$(pwd)
gather_dir=gather_info
datestamp=$(date +%Y%m%d_%H%M%S)
backup_folder=./backups
gather_dir_full_path=$current_dir/$gather_dir

if [[ ! -e $backup_folder ]]; then
  mkdir $backup_folder
fi

if [[ ! -e $gather_dir ]]; then
  mkdir $gather_dir
fi

# Cleanup existing vm_ip_info
if [[ -e $gather_dir/vm_ip_info ]]; then
  rm $gather_dir/vm_ip_info
fi

if [[ ! -e $gather_dir/vm_ip_info ]]; then
  touch $gather_dir/vm_ip_info
fi

cp $playbook_dir/$playbook_file $backup_folder/$playbook_file.$datestamp
cp $playbook_dir/$playbook_file $backup_folder/$playbook_file.backup
sed -i -e 's|replace_gather_dir|'$gather_dir_full_path'|' $playbook_dir/$playbook_file
# Execute provisioning playbook
ansible-playbook -i $gather_inventory $playbook_dir/$playbook_file

# Create copy of vm_ip_info
cp $gather_dir/vm_ip_info $gather_dir/ip_addys

# Cleanup formatting
sed -i -e 's|:||' $gather_dir/vm_ip_info
sed -i -e 's|None;|ansible_ssh_host=|' $gather_dir/vm_ip_info
sed -i -e 's|:||' $gather_dir/ip_addys
sed -i -e 's|None;||' $gather_dir/ip_addys

# Create ip hosts for importing SSH keys
awk '{print $2}' $gather_dir/ip_addys > $gather_dir/ip_hosts
sort -u $gather_dir/ip_hosts > $gather_dir/ip_hosts.ready

cp $gather_dir/ip_addys $gather_dir/ip_hostnames
awk '{print $1}' $gather_dir/ip_hostnames > $gather_dir/ip_hostnames.ready

# Import SSH keys new provisioned hosts into known_hosts
for node in $(cat $gather_dir/ip_hosts.ready); do
  ssh-keyscan $node >> ~/.ssh/known_hosts
done

# Import SSH keys new provisioned hosts into known_hosts
for node in $(cat $gather_dir/ip_hostnames.ready); do
  ssh-keyscan $node >> ~/.ssh/known_hosts
done

# Cleanup known_hosts for duplicate entries
sort -u ~/.ssh/known_hosts > ~/.ssh/known_hosts.clean
mv ~/.ssh/known_hosts ~/.ssh/known_hosts.backup
cp ~/.ssh/known_hosts.clean ~/.ssh/known_hosts

# Create new bootstrap hosts file to use for bootstrapping hosts
mv $gather_dir/vm_ip_info ./$host_inventory

mv $backup_folder/$playbook_file.backup $playbook_dir/$playbook_file
