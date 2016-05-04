#!/bin/bash
sudo apt-get update
sudo apt-get install -y git python-pip python-dev
sudo pip install ansible
ansible-galaxy install -r /vagrant/requirements.yml -f
sudo rm /etc/ansible/roles/ansible-es-filebeat
sudo ln -s /vagrant/ /etc/ansible/roles/ansible-es-filebeat
#ansible-playbook -i "localhost," -c local /vagrant/playbook.yml
