# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "rundeck" do |rundeck|
    rundeck.vm.box = "ubuntu/trusty64"
    rundeck.vm.hostname = "rundeck"

    rundeck.vm.network :private_network, ip: "192.168.202.201"
    rundeck.vm.network "forwarded_port", guest: 4440, host: 4440

    rundeck.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
  end
  config.vm.provision :shell, path: "provision.sh", keep_color: "true"
end
