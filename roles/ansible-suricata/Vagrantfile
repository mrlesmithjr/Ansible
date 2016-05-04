# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "suricata" do |suricata|
    suricata.vm.box = "ubuntu/trusty64"
    suricata.vm.hostname = "suricata"

    suricata.vm.network :private_network, ip: "192.168.202.201"

    suricata.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
  end
  config.vm.provision :shell, path: "provision.sh"
end
