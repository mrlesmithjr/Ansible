#!/bin/bash
sudo apt-get update
sudo apt-get install -y git python-pip python-dev
sudo pip install jinja2
sudo pip install ansible
sudo ansible-galaxy install -r /vagrant/requirements.yml -f
ansible-playbook -i "localhost," -c local /vagrant/playbook.yml
