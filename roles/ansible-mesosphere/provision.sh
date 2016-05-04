#!/bin/bash
if [ -f /etc/debian_version ]; then
  sudo apt-get update
  sudo apt-get install -y git python-pip python-dev
elif [ -f /etc/redhat-release ]; then
#  rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
  yum install -y epel-release
  yum install -y git python-pip python-devel python-dnf
fi
sudo pip install ansible
sudo rm /etc/ansible/roles/ansible-mesosphere
sudo mkdir -p /etc/ansible/roles
sudo ln -s /vagrant /etc/ansible/roles/ansible-mesosphere
sudo ansible-galaxy install -r /vagrant/requirements.yml -f
ansible-playbook -i /vagrant/hosts -c local /vagrant/playbook.yml
