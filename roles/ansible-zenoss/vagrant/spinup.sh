#!/bin/bash
ansible-galaxy install -r requirements.yml -f -p ./roles
vagrant up
ansible-playbook -i hosts zenoss.yml
