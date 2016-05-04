# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "gocdserver" do |gocdserver|
    gocdserver.vm.box = "mrlesmithjr/trusty64"
    gocdserver.vm.hostname = "gocdserver"

    gocdserver.vm.network :private_network, ip: "192.168.202.201"
    gocdserver.vm.network "forwarded_port", guest: 8153, host: 8153

    gocdserver.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
    gocdserver.vm.provision :shell, inline: 'ansible-galaxy install -r /vagrant/requirements.yml -f'
    gocdserver.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/playbook.yml --limit "gocdserver"'
  end
  config.vm.define "gocdagent" do |gocdagent|
    gocdagent.vm.box = "mrlesmithjr/trusty64"
    gocdagent.vm.hostname = "gocdagent"

    gocdagent.vm.network :private_network, ip: "192.168.202.202"

    gocdagent.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
    gocdagent.vm.provision :shell, inline: 'ansible-galaxy install -r /vagrant/requirements.yml -f'
    gocdagent.vm.provision :shell, inline: 'ansible-playbook -i /vagrant/hosts -c local /vagrant/playbook.yml --limit "gocdagent"'
  end
  config.vm.provision :shell, path: "provision.sh", keep_color: "true"
end
