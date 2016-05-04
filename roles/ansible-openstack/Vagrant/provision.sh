#!/bin/bash
sudo apt-get update
sudo apt-get install -y git python-pip python-dev
sudo pip install ansible==1.9.4
sudo ansible-galaxy install -r /vagrant/requirements.yml -f
#ansible-playbook -i "localhost," -c local /vagrant/playbook.yml
