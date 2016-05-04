# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.define "grafana" do |grafana|
    grafana.vm.box = "mrlesmithjr/trusty64"
    grafana.vm.hostname = "grafana"

    grafana.vm.network :private_network, ip: "192.168.202.201"
    grafana.vm.network "forwarded_port", guest: 80, host: 8080
    grafana.vm.network "forwarded_port", guest: 3000, host: 3000

    grafana.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
  end
  config.vm.provision :shell, path: "provision.sh", keep_color: "true"
end
