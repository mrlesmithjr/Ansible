#!/bin/bash
if [ -f /etc/debian_version ]; then
  sudo apt-get update
  sudo apt-get install -y git python-pip python-dev
  sudo pip install --upgrade pip
elif [ -f /etc/redhat-release ]; then
#  rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
  yum install -y epel-release
  yum install -y git python-pip python-devel python-dnf
fi
sudo pip install ansible
sudo ansible-galaxy install -r /vagrant/requirements.yml -f
ansible-playbook -i "localhost," -c local /vagrant/playbook.yml
