#!/bin/bash
sudo apt-get update
sudo apt-get -y install python-setuptools python-dev libffi-dev libssl-dev git sshpass tree
sudo easy_install pip
sudo pip install ansible==1.9.6
sudo ansible-galaxy install -r /vagrant/requirements.yml -f
ansible-playbook -i "localhost," -c local /vagrant/playbook.yml
