#!/bin/bash
site_file=site.yml
host_inventory=site_hosts

echo -n "Enter user account to use for deployment: "
read user_account

ansible-playbook -i $host_inventory $site_file --user $user_account --sudo
