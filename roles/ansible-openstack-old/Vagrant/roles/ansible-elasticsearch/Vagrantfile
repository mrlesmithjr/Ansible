# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "es1" do |es1|
    es1.vm.box = "mrlesmithjr/trusty64"
    es1.vm.hostname = "es1"

    es1.vm.network :private_network, ip: "192.168.202.201"
    es1.vm.network "forwarded_port", guest: 5600, host: 5600
    es1.vm.network "forwarded_port", guest: 9200, host: 9200
    es1.vm.network "forwarded_port", guest: 9300, host: 9300

    es1.vm.provider "virtualbox" do |vb|
     vb.memory = "1024"
    end
  end
  config.vm.provision :shell, path: "provision.sh"
end
