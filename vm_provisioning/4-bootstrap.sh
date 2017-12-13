#!/bin/bash
playbook_dir=./
playbook_file=bootstrap.yml
host_inventory=bootstrap_hosts
site_hosts_inventory=site_hosts
datestamp=$(date +%Y%m%d_%H%M%S)
backup_folder=./backups
gather_dir=gather_info
current_dir=$(pwd)

if [[ ! -e $gather_dir ]]; then
  mkdir $gather_dir
fi

if [[ ! -e $backup_folder ]]; then
  mkdir $backup_folder
fi

if [[ ! -e .ssh ]]; then
  mkdir .ssh
fi

# Bootstrap new hosts
cp $playbook_dir/$playbook_file $backup_folder/$playbook_file.backup
cp $playbook_dir/$playbook_file $backup_folder/$playbook_file.$datestamp

echo -n "Enter user account to create for logging into your hosts: "
read user_account
sed -i -e 's|replace_user|'$user_account'|' $playbook_dir/$playbook_file
stty -echo
echo -n "Enter password for account above: "
read user_password
user_pass_hash=$(echo -n $user_password|sha256sum|awk '{print $1}')
sed -i -e 's|replace_password|'$user_pass_hash'|' $playbook_dir/$playbook_file
ssh-keygen -b 2048 -t rsa -f .ssh/$user_account -q -N ""
chmod -R 600 .ssh/*
sed -i -e 's|replace_key_file|'$current_dir'/.ssh/'$user_account'.pub|' $playbook_dir/$playbook_file
stty echo
clear
# Run bootstrap playbook
ansible-playbook -i $host_inventory $playbook_dir/$playbook_file --user root --ask-pass

mv $backup_folder/$playbook_file.backup $playbook_dir/$playbook_file

if [[ -e ./site_hosts ]]; then
  mv ./site_hosts $backup_folder/site_hosts.$datestamp
fi

while read line
do
  printf "%s ansible_ssh_private_key_file=.ssh/$user_account\n" "$line" >> $site_hosts_inventory
done < $host_inventory

# add hosts to dns
#ansible-playbook -i bootstrap_hosts playbooks/update_dns_hosts_dnsmasq.yml --user remote --sudo
