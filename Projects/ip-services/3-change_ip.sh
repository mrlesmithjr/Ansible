#!/bin/bash
ansible-playbook -i bootstrap_hosts ./playbooks/change_ip.yml --user root --ask-pass

echo "Run 2-gather.sh after validating hosts have been rebooted and online"
