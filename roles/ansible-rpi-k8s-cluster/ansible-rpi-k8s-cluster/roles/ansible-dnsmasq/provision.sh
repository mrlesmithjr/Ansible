#!/bin/bash
sudo apt-get update
sudo apt-get install -y git python-pip python-dev
sudo pip install jinja2
sudo pip install ansible
sudo ansible-galaxy install -r /vagrant/requirements.yml -f
#sudo mkdir -p /etc/ansible/roles
#sudo git clone --branch=dev https://github.com/mrlesmithjr/ansible-dnsmasq.git /etc/ansible/roles/ansible-dnsmasq
ansible-playbook -i "localhost," -c local /vagrant/playbook.yml
