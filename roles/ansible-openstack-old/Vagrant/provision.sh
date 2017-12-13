#!/bin/bash
sudo apt-get update
sudo apt-get install -y python-setuptools python-dev libffi-dev libssl-dev git sshpass tree
sudo easy_install pip
sudo pip install -U setuptools
sudo pip install ansible==1.9.6 #Needs to remain this version due to pacemaker module
#sudo ansible-galaxy install -r /vagrant/requirements.yml -f
