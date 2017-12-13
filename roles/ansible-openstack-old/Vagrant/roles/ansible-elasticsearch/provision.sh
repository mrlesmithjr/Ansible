#!/bin/bash
sudo apt-get update
sudo apt-get install -y git python-pip python-dev
sudo pip install jinja2
sudo pip install ansible
#mkdir -p /opt/ansible-playbooks/roles
sudo git clone --depth=50 --branch=2.1 https://github.com/mrlesmithjr/ansible-elasticsearch.git /etc/ansible/roles/ansible-elasticsearch
#sudo cp /vagrant/playbook.yml /opt/ansible-playbooks
ansible-playbook -i "localhost," -c local /vagrant/playbook.yml --extra-vars "es_docker_install: false"
