#!/bin/bash
sudo apt-get update
sudo apt-get install -y git python-pip python-dev
sudo pip install jinja2
sudo pip install ansible
sudo ansible-galaxy install -r /vagrant/requirements.yml -f
#sudo git clone --depth=50 --branch=dev https://github.com/mrlesmithjr/ansible-owncloud.git /etc/ansible/roles/ansible-owncloud
ansible-playbook -i "localhost," -c local /vagrant/playbook.yml
