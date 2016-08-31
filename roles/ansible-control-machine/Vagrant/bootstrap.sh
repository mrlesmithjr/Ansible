#!/bin/bash
if [ -f /etc/debian_version ]; then
  codename="$(lsb_release -c | awk {'print $2}')"
  if [[ $codename == "vivid" ]]; then
    sudo apt-get update && \
    sudo apt-get -y install python-simplejson
  fi
  if [[ $codename == "wily" ]]; then
    sudo apt-get update && \
    sudo apt-get -y install python-simplejson
  fi
  if [[ $codename == "xenial" ]]; then
    sudo apt-get update && \
    sudo apt-get -y install python-simplejson
  fi
  sudo apt-get -y install python-setuptools python-dev python-pip libffi-dev libssl-dev git sshpass tree
  sudo pip install virtualenv
  mkdir ~/ansible_virtualenv
  cd ~/ansible_virtualenv
  virtualenv ansible-2.1.1.0
  source ansible-2.1.1.0/bin/activate
  pip install ansible==2.1.1.0
  ansible-playbook -i "localhost," -c local /vagrant/playbook.yml
fi
if [ -f /etc/redhat-release ]; then
  codename="$(gawk -F= '/^NAME/{print $2}' /etc/os-release)"
  if [[ $codename == "Fedora" ]]; then
    sudo dnf -y install python-devel python-dnf && \
    sudo dnf -y group install "C Development Tools and Libraries"
  fi
fi
