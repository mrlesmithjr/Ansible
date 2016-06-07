#!/bin/bash
sudo apt-get update
sudo apt-get install -y git libffi-dev libssl-dev python-dev python-setuptools
sudo easy_install pip
sudo pip install ansible==1.9.6
sudo ansible-galaxy install -r /vagrant/requirements.yml -f
#ansible-playbook -i "localhost," -c local /vagrant/playbook.yml
