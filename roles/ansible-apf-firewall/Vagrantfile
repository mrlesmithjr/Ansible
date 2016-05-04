# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "apf" do |apf|
    apf.vm.box = "mrlesmithjr/trusty64"
    apf.vm.hostname = "apf"

#    apf.vm.network :private_network, ip: "192.168.202.201"

    apf.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
  end
  config.vm.provision :shell, path: "provision.sh", keep_color: "true"
end
